import requests
from collections import defaultdict

# Replace with your Codeforces handle
handle = "your_handle"

url = f"https://codeforces.com/api/user.status?handle=NovaStorm37"
response = requests.get(url)
data = response.json()

if data['status'] != 'OK':
    print("Error fetching data. Check your handle.")
    exit()

# Using a set to avoid duplicate problems
solved = {}
for sub in data['result']:
    if sub['verdict'] == 'OK':
        prob = sub['problem']
        pid = f"{prob.get('contestId', '')}{prob.get('index', '')}"
        if pid not in solved:
            solved[pid] = {
                'name': prob.get('name'),
                'rating': prob.get('rating', 'Unrated'),
                'tags': prob.get('tags', [])
            }

# Grouping problems by tags
tag_groups = defaultdict(list)
for pid, details in solved.items():
    tags = details['tags']
    if not tags:
        tag_groups['Untagged'].append((pid, details['name'], details['rating']))
    else:
        for tag in tags:
            tag_groups[tag].append((pid, details['name'], details['rating']))

# Printing results
for tag in sorted(tag_groups):
    print(f"\n🔖 Tag: {tag} ({len(tag_groups[tag])} problems)")
    print("-" * 60)
    for pid, name, rating in sorted(tag_groups[tag], key=lambda x: (x[2] if isinstance(x[2], int) else 0, x[0])):
        print(f"• {pid}: {name} [Rating: {rating}]")

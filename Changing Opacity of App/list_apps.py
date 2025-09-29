import pygetwindow as gw

# Getting all window titles
window_list = gw.getAllTitles()

# Printing the titles
for i, title in enumerate(window_list):
    if title:  # Ignoring empty window titles
        print(f"{i+1}. {title}")

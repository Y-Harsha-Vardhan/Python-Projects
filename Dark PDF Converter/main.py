# Usage python3 main.py file.pdf, after navigating to current directory in terminal.

#!/usr/bin/env python3
import subprocess
import sys
import os

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} input.pdf [output.pdf]")
        sys.exit(1)

    # Hard‑coded Ghostscript executable path
    gs = r"C:\Program Files\gs\gs10.05.1\bin\gswin64c.exe"
    if not os.path.isfile(gs):
        print(f"Error: Ghostscript executable not found at:\n  {gs}")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2] if len(sys.argv) > 2 else "inverted.pdf"

    cmd = [
        gs,
        "-q",
        "-dNOPAUSE", "-dBATCH",
        "-sDEVICE=pdfwrite",
        "-o", output_pdf,
        # Four exch‑sub blocks for CMYK, then setcolortransfer
        "-c", "{1 exch sub}{1 exch sub}{1 exch sub}{1 exch sub} setcolortransfer",
        "-f", input_pdf
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Created inverted PDF → {output_pdf}")
    except subprocess.CalledProcessError as e:
        print("❌ Ghostscript failed:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()

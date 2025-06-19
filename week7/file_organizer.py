#!/usr/bin/env python3
"""
file_organizer.py
─────────────────
A local-automation demo for COSC 1104 Week 7.
• Scans a target directory (default: the current working dir)
• Creates sub-folders by file extension   (e.g.  Pictures/, Docs/, Code/)
• Moves each file into the matching sub-folder
• Renames files so that any spaces become underscores
• Prints a tidy summary of everything it did
"""

from pathlib import Path
from datetime import datetime
import shutil
import os
import sys

# ---------- 1.  Configuration ---------------------------------------------
# Map file extensions to human-friendly folder names.
DEST_FOLDERS = {
    # images
    ".jpg": "Pictures", ".jpeg": "Pictures", ".png": "Pictures",
    ".gif": "Pictures", ".bmp": "Pictures", ".svg": "Pictures",
    # documents
    ".pdf": "Docs", ".doc": "Docs", ".docx": "Docs",
    ".txt": "Docs", ".md": "Docs", ".rtf": "Docs",
    # data / spreadsheets
    ".csv": "Data", ".xls": "Data", ".xlsx": "Data",
    # code
    ".java": "Code", ".cpp": "Code",
    ".js": "Code", ".html": "Code", ".css": "Code",
    # compressed
    ".zip": "Archives", ".tar": "Archives", ".gz": "Archives",
}

# ---------- 2.  Utility helpers -------------------------------------------
def nice_time() -> str:
    """Return current time as HH:MM:SS string for logging."""
    return datetime.now().strftime("%H:%M:%S")

def safe_move(src: Path, dest_dir: Path) -> None:
    """
    Move *src* into *dest_dir*, renaming if a file of the same name exists.
    Spaces in the filename are replaced with underscores.
    """
    dest_dir.mkdir(exist_ok=True)
    new_name = src.name.replace(" ", "_")
    candidate = dest_dir / new_name

    counter = 1
    while candidate.exists():
        stem, ext = os.path.splitext(new_name)
        candidate = dest_dir / f"{stem}_{counter}{ext}"
        counter += 1

    shutil.move(str(src), candidate)
    print(f"[{nice_time()}]  Moved → {candidate.relative_to(Path.cwd())}")

# ---------- 3.  Main logic -------------------------------------------------
def organize(folder: Path) -> None:
    """Scan *folder* and organize its files."""
    print(f"\n[{nice_time()}]  Starting in: {folder.resolve()}\n")

    moved = 0
    for path in folder.iterdir():
        # Skip directories (including any we created earlier)
        if path.is_dir():
            continue

        ext = path.suffix.lower()
        dest_name = DEST_FOLDERS.get(ext, "Other")
        dest_dir = folder / dest_name

        safe_move(path, dest_dir)
        moved += 1

    print(f"\n[{nice_time()}]  Done. {moved} file(s) organized.\n")

# ---------- 4.  CLI wrapper ------------------------------------------------
if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    if not target.is_dir():
        sys.exit("Error: supplied path is not a directory.")

    organize(target)

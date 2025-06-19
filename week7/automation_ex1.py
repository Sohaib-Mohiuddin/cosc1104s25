import os
import glob

# Get list of all .txt files in current directory
txt_files = glob.glob("*.txt")

print("Renaming files...")
for index, filename in enumerate(txt_files, start=1):
    new_name = f"file_{index}.txt"
    os.rename(filename, new_name)
    print(f"{filename} -> {new_name}")

print("Done!")

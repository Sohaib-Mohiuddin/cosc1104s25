import os
from datetime import datetime

# Get current date and time
now = datetime.now()
# 2025-06-19 13:35:10
print(f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Get directory contents
contents = os.listdir('.')
print(contents)

# Save to file
with open("directory_contents.txt", "w") as f:
    for item in contents:
        f.write(item + "\n")

print("Directory contents saved to directory_contents.txt")

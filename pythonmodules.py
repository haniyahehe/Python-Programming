# os Module
import os

print("# Current Working Directory:")
print(os.getcwd())

# List All Files & Folders
print("\n# List of Files and Folders:")
print(os.listdir())

# Create A New Folder
# If The Folder Already Exists, This Will Raise An Error
if not os.path.exists("new_folder"):
    os.mkdir("new_folder")
    print("\n# 'new_folder' has been created.")
else:
    print("\n# 'new_folder' already exists.")

# Rename A Folder (From 'new_folder' To 'renamed_folder')
if os.path.exists("new_folder"):
    os.rename("new_folder", "renamed_folder")
    print("\n# Folder renamed to 'renamed_folder'.")

# Remove The Renamed Folder
if os.path.exists("renamed_folder"):
    os.rmdir("renamed_folder")
    print("\n# 'renamed_folder' has been deleted.")


# Math Module
import math

angle_deg = 90
angle_rad = math.radians(angle_deg)

# Sin, Cos, Tan
print(f"# sin({angle_deg}) = {math.sin(angle_rad)}")
print(f"# cos({angle_deg}) = {math.cos(angle_rad)}")
print(f"# tan({angle_deg}) = {math.tan(angle_rad)}")
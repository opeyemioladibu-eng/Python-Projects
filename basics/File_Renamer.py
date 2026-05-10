import os
folder_path = input("Enter Folder Path: ")
files = os.listdir(folder_path)
count = 1
for file in files:
    if file.endswith(".txt"):
        old_path = os.path.join(folder_path, file)
        new_name = f"file_{count}.txt"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        count += 1
        

print("Files renamed.")
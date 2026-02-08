import os

# Specify the directory you want to list
directory_path = '/'

try:
    # os.listdir() returns a list of entries (files + folders) in the directory
    contents = os.listdir(directory_path)

    print(f"Contents of '{directory_path}':")
    for item in contents:
        print(item)

except Exception as e:
    print("Error:", e)

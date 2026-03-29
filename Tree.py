import os

def print_tree(start_path, file, prefix=""):
    try:
        items = sorted(os.listdir(start_path))
    except PermissionError:
        file.write(prefix + "└── [Permission Denied]\n")
        return

    pointers = ['├── '] * (len(items) - 1) + ['└── '] if items else []

    for pointer, item in zip(pointers, items):
        path = os.path.join(start_path, item)

        file.write(prefix + pointer + item + ('/' if os.path.isdir(path) else '') + "\n")

        if os.path.isdir(path):
            extension = '│   ' if pointer == '├── ' else '    '
            print_tree(path, file, prefix + extension)


# Ask user for folder path
folder_path = input("Enter folder path: ").strip()

# Ask output file name
output_file = input("Enter output file name (example tree.txt): ").strip()

# Validate path
if not os.path.exists(folder_path):
    print("❌ Path does not exist")

elif not os.path.isdir(folder_path):
    print("❌ Path is not a folder")

else:
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(folder_path + "\n")
        print_tree(folder_path, f)

    print(f"✅ Tree saved to {output_file}")

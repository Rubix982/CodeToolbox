import os


def get_folder_size(folder_path):
    """
    Calculate the total size of a folder in bytes.

    Args:
        folder_path (str): Path to the folder.

    Returns:
        int: Total size of the folder in bytes.
    """
    total_size = 0
    for dirpath, _, filenames in os.walk(folder_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size


def list_folder_sizes(directory_path):
    """
    List the sizes of all folders within a directory in MB.

    Args:
        directory_path (str): Path to the parent directory.
    """
    if not os.path.isdir(directory_path):
        print(f"The provided path '{directory_path}' is not a valid directory.")
        return

    print(f"Sizes of folders in '{directory_path}':")
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            folder_size = get_folder_size(item_path) / (
                1024 * 1024
            )  # Convert bytes to MB
            print(f"{item}: {folder_size:.2f} MB")


if __name__ == "__main__":
    directory_path = input("Enter the directory path: ").strip()
    list_folder_sizes(directory_path)

import os
import json


def minify_json_files(folder_path):
    """
    Minifies all JSON files in the specified folder path recursively.

    Args:
        folder_path (str): Path to the folder containing JSON files.
    """
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json") or file.endswith('.jsonc'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as json_file:
                        data = json.load(json_file)

                    with open(file_path, "w", encoding="utf-8") as json_file:
                        json.dump(
                            data, json_file, separators=(",", ":"), ensure_ascii=False
                        )

                    print(f"Minified: {file_path}")
                except (json.JSONDecodeError, IOError) as e:
                    print(f"Failed to process {file_path}: {e}")


if __name__ == "__main__":
    folder_path = input("Enter the folder path containing JSON files: ").strip()
    if os.path.isdir(folder_path):
        minify_json_files(folder_path)
    else:
        print("The provided path is not a valid directory.")

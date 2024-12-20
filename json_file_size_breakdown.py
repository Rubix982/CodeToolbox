import json
import os
from sys import getsizeof

def analyze_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    def analyze(data, path="root"):
        if isinstance(data, dict):
            for key, value in data.items():
                analyze(value, f"{path}.{key}")
        elif isinstance(data, list):
            print(f"{path} - List of {len(data)} items - Size: {getsizeof(data)} bytes")
            for index, item in enumerate(data[:10]):  # Show first 10 items for clarity
                analyze(item, f"{path}[{index}]")
        else:
            print(f"{path} - Value: {data} - Size: {getsizeof(data)} bytes")

    analyze(data)

file_path = input("Enter JSON file path: ").strip()
if os.path.isfile(file_path):
    analyze_json(file_path)
else:
    print("Invalid file path.")

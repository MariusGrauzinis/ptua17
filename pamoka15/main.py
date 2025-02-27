import json
import logging
from typing import Optional

logging.basicConfig(filename='app.log', level=logging.ERROR)

def read_file_as_string(filename: str) -> Optional[str]:
    try:
        with open(filename, 'r') as file:
            return file.read()
    except Exception as e:
        logging.error(f"Error reading file {filename}: {e}")
        return None

def parse_json_string(data: str) -> Optional[dict]:
    try:
        return json.loads(data)
    except json.JSONDecodeError as e:
        logging.error(f"Error parsing JSON: {e}")
        return None

def main():
    filename = input("Enter file name (pvz., test.json): ")

    file_content = read_file_as_string(filename)

    if file_content:
        data = parse_json_string(file_content)

        if data:
            print("Successfully loaded JSON data:", data)
        else:
            print("Failed to load JSON data.")
    else:
        print("Failed to read the file.")

if __name__ == "__main__":
    main()
def read_file_as_string(filename: str) -> Optional[str]:
    """
    Reads the contents of a file into a string.
    Returns the file contents as a string on success, or None on failure.
    """
    pass

def parse_json_string(data: str) -> Optional[dict]:
    """
    Attempts to parse a JSON string into a dictionary.
    Returns the dictionary on success, or None on failure.
    """
    pass

Implement main.py with a logic. so that user can enter file name for example : test.json. 
You need to use two functions above to read file and parse that json and print output into terminal like this
print("Successfully loaded JSON data:", data)
 
otherwise:
 
print("Failed to load JSON data.")
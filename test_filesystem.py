import sys
import os
from pathlib import Path

# Add the runtime path to the system path
sys.path.append(str(Path(__file__).parent / 'runtime' / 'tools'))

from filesystem import FileSystemTool

def run_test():
    """
    Tests the FileSystemTool functionality.
    """
    fs = FileSystemTool()
    test_file = Path("hello.txt")
    
    # Clean up previous test runs if file exists
    if test_file.exists():
        test_file.unlink()

    # 1. Write a file
    print("Writing file...")
    fs.write_file(test_file, "Hello World")

    # 2. Read the file
    print("Reading...")
    content = fs.read_file(test_file)
    print(content)

    # 3. Append to the file
    print("\nAppending...")
    fs.append_file(test_file, "\nSecond Line")

    # 4. Read the appended file
    appended_content = fs.read_file(test_file)
    print(appended_content)


    # 5. List the directory
    print("Listing...")
    dir_contents = fs.list_directory(".")
    # Filter for the test file to avoid printing other files in the directory
    if test_file.name in dir_contents:
        print(test_file.name)

    # Clean up the test file
    if test_file.exists():
        test_file.unlink()

if __name__ == "__main__":
    run_test()

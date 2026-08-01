from pathlib import Path
from typing import List, Union

class FileSystemTool:
    """A tool for interacting with the file system."""

    def read_file(self, path: Union[str, Path]) -> str:
        """
        Reads the content of a file.

        Args:
            path: The path to the file.

        Returns:
            The content of the file as a string.
        """
        try:
            return Path(path).read_text()
        except FileNotFoundError:
            return f"Error: File not found at {path}"
        except Exception as e:
            return f"Error reading file: {e}"

    def write_file(self, path: Union[str, Path], content: str) -> str:
        """
        Writes content to a file. Overwrites the file if it exists.

        Args:
            path: The path to the file.
            content: The content to write.
        
        Returns:
            A confirmation message.
        """
        try:
            Path(path).write_text(content)
            return f"File written to {path}"
        except Exception as e:
            return f"Error writing file: {e}"

    def append_file(self, path: Union[str, Path], text: str) -> str:
        """
        Appends text to a file.

        Args:
            path: The path to the file.
            text: The text to append.
        
        Returns:
            A confirmation message.
        """
        try:
            with open(path, "a") as f:
                f.write(text)
            return f"Text appended to {path}"
        except Exception as e:
            return f"Error appending to file: {e}"

    def create_folder(self, path: Union[str, Path]) -> str:
        """
        Creates a directory.

        Args:
            path: The path to the directory to create.
            
        Returns:
            A confirmation message.
        """
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            return f"Folder created at {path}"
        except Exception as e:
            return f"Error creating folder: {e}"

    def list_directory(self, path: Union[str, Path]) -> List[str]:
        """
        Lists the contents of a directory.

        Args:
            path: The path to the directory.

        Returns:
            A list of file and directory names.
        """
        try:
            return [str(p.name) for p in Path(path).iterdir()]
        except FileNotFoundError:
            return [f"Error: Directory not found at {path}"]
        except Exception as e:
            return [f"Error listing directory: {e}"]

    def exists(self, path: Union[str, Path]) -> bool:
        """
        Checks if a path exists.

        Args:
            path: The path to check.

        Returns:
            True if the path exists, False otherwise.
        """
        return Path(path).exists()

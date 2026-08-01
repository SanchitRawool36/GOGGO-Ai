from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent))

from filesystem import FileSystemTool


def run_demo() -> str:
    """Run a simple filesystem smoke test and return a summary message."""
    fs = FileSystemTool()
    temp_file = Path("python_runner_demo.txt")

    if temp_file.exists():
        temp_file.unlink()

    fs.write_file(temp_file, "Hello from PythonRunner")
    content = fs.read_file(temp_file)
    fs.append_file(temp_file, "\nAppended")
    updated = fs.read_file(temp_file)
    files = fs.list_directory(".")

    if temp_file.exists():
        temp_file.unlink()

    return (
        "PythonRunner demo completed. "
        f"Read={content!r}; Updated={updated!r}; Files={files}"
    )


if __name__ == "__main__":
    print(run_demo())

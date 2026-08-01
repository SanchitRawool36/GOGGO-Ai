from pathlib import Path
import subprocess
import sys


class PythonRunner:
    """
    Executes Python code or Python files.
    """

    def run(self, code: str):
        """
        Execute inline Python code.
        """

        result = subprocess.run(
            [sys.executable, "-c", code],
            capture_output=True,
            text=True,
        )

        return result.stdout if result.stdout else result.stderr

    def run_file(self, filename: str):
        """
        Execute a Python file.
        """

        result = subprocess.run(
            [sys.executable, filename],
            capture_output=True,
            text=True,
        )

        return result.stdout if result.stdout else result.stderr
import subprocess
import traceback

from runtime.tools.filesystem import FileSystemTool
from runtime.self_healing.error_fixer import ErrorFixer


class SelfHealer:

    def __init__(self, router):

        self.router = router
        self.fs = FileSystemTool()
        self.fixer = ErrorFixer(router)

    def run(self, filename, retries=3):

        for attempt in range(retries):

            result = subprocess.run(
                ["python", filename],
                capture_output=True,
                text=True,
            )

            if result.returncode == 0:

                print("Execution Successful")

                print(result.stdout)

                return True

            print(f"\nAttempt {attempt+1} failed")

            print(result.stderr)

            code = self.fs.read_file(filename)

            fixed = self.fixer.fix(
                code,
                result.stderr,
            )

            self.fs.write_file(
                filename,
                fixed,
            )

            print("Code Rewritten\n")

        print("Maximum retries reached.")

        return False
from pathlib import Path

from runtime.tools.tool_manager import ToolManager


class ActionExecutor:

    def __init__(self):
        self.tools = ToolManager()

    # -------------------------------------------------
    # Execute Existing Python File
    # -------------------------------------------------

    def execute_python(self, filename: str):

        python = self.tools.get("python")

        print(f"\nRunning: {filename}")

        return python.run_file(filename)

    # -------------------------------------------------
    # Save + Execute
    # -------------------------------------------------

    def save_and_execute(self, filename: str, code: str):

        filesystem = self.tools.get("filesystem")

        filesystem.write_file(filename, code)

        print(f"\nSaved: {filename}")

        return self.execute_python(filename)

    # -------------------------------------------------

    def execute_shell(self, command: str):

        shell = self.tools.get("shell")

        return shell.run(command)

    # -------------------------------------------------

    def git_status(self):

        git = self.tools.get("git")

        return git.status()

    # -------------------------------------------------

    def git_commit(self, message="AI Update"):

        git = self.tools.get("git")

        git.add()

        git.commit(message)

        return "Commit Complete"

    # -------------------------------------------------

    def git_push(self):

        git = self.tools.get("git")

        git.push()

        return "Push Complete"
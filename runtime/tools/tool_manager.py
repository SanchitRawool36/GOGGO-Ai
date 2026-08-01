from __future__ import annotations

from typing import Dict, Any

from runtime.tools.filesystem import FileSystemTool
from runtime.tools.git_tool import add, commit, push, status
from runtime.tools.shell import ShellTool
from runtime.tools.python_runner import PythonRunner


class GitToolAdapter:
    """
    Adapter class that exposes Git operations
    through a simple object interface.
    """

    def status(self, repo_path: str = ".") -> str:
        return status(repo_path)

    def add(self, repo_path: str = ".", files=None) -> str:
        return add(repo_path, files)

    def commit(self, repo_path: str = ".", message: str = "chore: update") -> str:
        return commit(repo_path, message)

    def push(self, repo_path: str = ".") -> str:
        return push(repo_path)


class ToolManager:
    """
    Central registry for every tool available
    to AI agents.
    """

    def __init__(self):

        self._tools: Dict[str, Any] = {

            "filesystem": FileSystemTool(),

            "git": GitToolAdapter(),

            "shell": ShellTool(),

            "python": PythonRunner(),

        }

    # -------------------------
    # Get Tool
    # -------------------------

    def get(self, name: str):

        tool = self._tools.get(name)

        if tool is None:
            raise KeyError(f"Unknown tool: {name}")

        return tool

    # -------------------------
    # List Tools
    # -------------------------

    def list_tools(self):

        return list(self._tools.keys())

    # -------------------------
    # Check Tool Exists
    # -------------------------

    def has(self, name: str):

        return name in self._tools

    # -------------------------
    # Register New Tool
    # -------------------------

    def register(self, name: str, tool):

        self._tools[name] = tool

    # -------------------------
    # Remove Tool
    # -------------------------

    def unregister(self, name: str):

        if name in self._tools:
            del self._tools[name]

    # -------------------------
    # Execute Tool Method
    # -------------------------

    def execute(self, tool_name: str, method_name: str, *args, **kwargs):

        tool = self.get(tool_name)

        if not hasattr(tool, method_name):
            raise AttributeError(
                f"{tool_name} has no method '{method_name}'"
            )

        method = getattr(tool, method_name)

        return method(*args, **kwargs)
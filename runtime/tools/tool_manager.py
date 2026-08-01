from __future__ import annotations

from typing import Dict, Optional

from runtime.tools.filesystem import FileSystemTool
from runtime.tools.git_tool import add, commit, push, status
from runtime.tools.shell import ShellTool


class ToolManager:
    """Registry-style manager for runtime tools."""

    def __init__(self):
        self._tools: Dict[str, object] = {
            "filesystem": FileSystemTool(),
            "git": GitToolAdapter(),
            "shell": ShellTool(),
            "python": ShellTool(),
        }

    def run(self, name: str, *args, **kwargs):
        tool = self._tools.get(name)
        if tool is None:
            raise KeyError(f"Unknown tool: {name}")
        return tool


class GitToolAdapter:
    """Simple adapter for git operations."""

    def status(self, repo_path: str = ".") -> str:
        return status(repo_path)

    def add(self, repo_path: str = ".", files=None) -> str:
        return add(repo_path, files)

    def commit(self, repo_path: str = ".", message: str = "chore: update") -> str:
        return commit(repo_path, message)

    def push(self, repo_path: str = ".") -> str:
        return push(repo_path)

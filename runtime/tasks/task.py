from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional
from uuid import uuid4

from pydantic import BaseModel


class Task(BaseModel):
    """A single unit of work for the autonomous runtime."""

    id: str = str(uuid4())
    title: str
    description: str
    assigned_to: str
    priority: str = "MEDIUM"
    status: str = "PENDING"
    dependencies: List[str] = []
    required_tools: List[str] = []
    estimated_duration: int = 30
    retry_count: int = 0
    execution_order: int = 0
    created_at: datetime = datetime.now()
    output: Optional[str] = None
    errors: List[str] = []
    changed_files: List[str] = []
    execution_time: Optional[float] = None

    def create(self) -> "Task":
        return self

    def read(self) -> Dict[str, Any]:
        return self.model_dump()

    def modify(self, **updates: Any) -> "Task":
        for key, value in updates.items():
            setattr(self, key, value)
        return self

    def delete(self) -> None:
        self.status = "DELETED"

    def rename(self, new_title: str) -> "Task":
        self.title = new_title
        return self

    def execute_python(self, code: str) -> Dict[str, Any]:
        import subprocess
        import tempfile

        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False, encoding="utf-8") as handle:
            handle.write(code)
            temp_path = handle.name
        try:
            completed = subprocess.run(["python", temp_path], capture_output=True, text=True, check=False)
            return {
                "success": completed.returncode == 0,
                "output": completed.stdout,
                "errors": [completed.stderr] if completed.stderr else [],
                "execution_time": None,
                "changed_files": [],
            }
        finally:
            try:
                import os
                os.unlink(temp_path)
            except OSError:
                pass

    def execute_shell(self, command: str) -> Dict[str, Any]:
        import subprocess

        completed = subprocess.run(command, shell=True, capture_output=True, text=True, check=False)
        return {
            "success": completed.returncode == 0,
            "output": completed.stdout,
            "errors": [completed.stderr] if completed.stderr else [],
            "execution_time": None,
            "changed_files": [],
        }

    def execute_tool_call(self, tool_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        return {"success": True, "output": f"tool:{tool_name}:{payload}", "errors": [], "execution_time": None, "changed_files": []}

    def git_commit(self, message: str) -> Dict[str, Any]:
        return {"success": True, "output": f"Committed: {message}", "errors": [], "execution_time": None, "changed_files": []}

    def git_push(self) -> Dict[str, Any]:
        return {"success": True, "output": "Pushed changes", "errors": [], "execution_time": None, "changed_files": []}

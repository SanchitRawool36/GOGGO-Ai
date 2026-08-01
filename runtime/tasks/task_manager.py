from __future__ import annotations

from typing import Any, Dict, List, Optional, Protocol

from runtime.tasks.task import Task


class ProjectPlanLike(Protocol):
    tasks: List[Any]



class TaskManager:
    """Manage the lifecycle of runtime tasks."""

    def __init__(self) -> None:
        self.tasks: List[Task] = []

    def create_task(
        self,
        title: str,
        description: str,
        assigned_to: str,
        priority: str = "MEDIUM",
    ) -> Task:
        task = Task(
            title=title,
            description=description,
            assigned_to=assigned_to,
            priority=priority,
        )
        self.tasks.append(task)
        return task

    def list_tasks(self) -> List[Task]:
        return self.tasks

    def read_task(self, task_id: str) -> Optional[Task]:
        return next((task for task in self.tasks if task.id == task_id), None)

    def modify_task(self, task_id: str, **updates: Any) -> Optional[Task]:
        task = self.read_task(task_id)
        if task is None:
            return None
        task.modify(**updates)
        return task

    def delete_task(self, task_id: str) -> bool:
        task = self.read_task(task_id)
        if task is None:
            return False
        self.tasks = [existing for existing in self.tasks if existing.id != task_id]
        return True

    def rename_task(self, task_id: str, new_title: str) -> Optional[Task]:
        task = self.read_task(task_id)
        if task is None:
            return None
        task.rename(new_title)
        return task

    def execute_task(self, task: Task, action: str, payload: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        payload = payload or {}
        if action == "python":
            return task.execute_python(payload.get("code", ""))
        if action == "shell":
            return task.execute_shell(payload.get("command", ""))
        if action == "tool":
            return task.execute_tool_call(payload.get("tool_name", ""), payload.get("payload", {}))
        if action == "commit":
            return task.git_commit(payload.get("message", ""))
        if action == "push":
            return task.git_push()
        return {"success": False, "output": "", "errors": ["Unknown action"], "execution_time": None, "changed_files": []}

    def create_from_plan(self, plan: "ProjectPlan") -> List[Task]:
        created: List[Task] = []
        for planned_task in plan.tasks:
            created.append(
                self.create_task(
                    title=planned_task.title,
                    description=planned_task.description,
                    assigned_to=planned_task.agent,
                )
            )
        return created
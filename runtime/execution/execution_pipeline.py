from __future__ import annotations

from typing import Any, Dict, List

from runtime.agents.agent_manager import AgentManager
from runtime.planner.planner import Planner
from runtime.tasks.task_manager import TaskManager


class ExecutionPipeline:
    """Coordinate planning, delegation, execution, and reflection for runtime tasks."""

    def __init__(self) -> None:
        self.planner = Planner()
        self.task_manager = TaskManager()
        self.agent_manager = AgentManager()

    def run(self, goal: str) -> Dict[str, Any]:
        plan = self.planner.create_plan(goal)
        tasks = []
        for item in plan.get("tasks", []):
            task = self.task_manager.create_task(
                title=item["title"],
                description=item["description"],
                assigned_to=item.get("agent", "CTO"),
                priority=item.get("priority", "MEDIUM"),
            )
            tasks.append(task)
        return {"goal": goal, "plan": plan, "tasks": [task.dict() for task in tasks]}

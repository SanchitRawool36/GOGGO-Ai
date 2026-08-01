from __future__ import annotations
from typing import TYPE_CHECKING
from runtime.tasks.task import Task

if TYPE_CHECKING:
    from runtime.planner.planner import ProjectPlan


class TaskManager:

    def __init__(self):
        self.tasks = []

    def create_task(
        self,
        title,
        description,
        assigned_to,
        priority="MEDIUM",
    ):

        task = Task(
            title=title,
            description=description,
            assigned_to=assigned_to,
            priority=priority,
        )

        self.tasks.append(task)

        return task

    def list_tasks(self):
        return self.tasks

    def create_from_plan(self, plan: ProjectPlan):
        for planned_task in plan.tasks:
            self.create_task(
                title=planned_task.title,
                description=planned_task.description,
                assigned_to=planned_task.agent,
            )
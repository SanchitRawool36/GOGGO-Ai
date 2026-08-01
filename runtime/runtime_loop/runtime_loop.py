from __future__ import annotations

from typing import Optional

from runtime.collaboration.collaboration import Collaboration
from runtime.memory.memory_manager import MemoryManager
from runtime.planner.planner import Planner
from runtime.tasks.inbox import Inbox
from runtime.tasks.task_manager import TaskManager


class RuntimeLoop:
    """Simple orchestration loop for the autonomous runtime."""

    def __init__(self):
        self.inbox = Inbox()
        self.planner = Planner()
        self.task_manager = TaskManager()
        self.collaboration = Collaboration()
        self.memory = MemoryManager()

    def run_once(self, goal: str) -> Optional[str]:
        """Process a single goal through planning, task creation, collaboration, and memory."""
        plan = self.planner.create_plan(goal)
        self.task_manager.create_from_plan(plan)
        for task in self.task_manager.list_tasks():
            self.collaboration.execute(task)
        self.memory.save()
        return plan.goal

    def run_forever(self) -> None:
        """Run the main loop indefinitely."""
        while True:
            goal = self.inbox.next()
            if goal is None:
                break
            self.run_once(goal if isinstance(goal, str) else str(goal))


if __name__ == "__main__":
    RuntimeLoop().run_forever()
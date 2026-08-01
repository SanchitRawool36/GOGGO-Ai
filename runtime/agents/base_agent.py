from runtime.router.model_router import ModelRouter
from runtime.tasks.inbox import Inbox


class BaseAgent:

    def __init__(
        self,
        name: str,
        role: str,
        system_prompt: str,
        model: str | None = None,
    ):

        self.name = name
        self.role = role
        self.system_prompt = system_prompt

        self.router = ModelRouter(model)
        self.inbox = Inbox()

    def run(self, task: str):

        prompt = f"""
SYSTEM

{self.system_prompt}

USER

{task}
"""

        return self.router.ask(prompt)

    def assign_task(self, task):
        self.inbox.add(task)

    def work(self):

        task = self.inbox.next()

        if task is None:
            return "No pending tasks."

        task.status = "IN_PROGRESS"

        answer = self.run(task.description)

        task.status = "COMPLETED"

        return answer
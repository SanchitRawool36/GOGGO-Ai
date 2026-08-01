from runtime.core.logger import logger
from runtime.router.model_router import ModelRouter
from runtime.tasks.inbox import Inbox
from runtime.tools.tool_manager import ToolManager

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
        self.tools = ToolManager()
        self.inbox = Inbox()

    def run(self, task: str):

        prompt = f"""
SYSTEM

{self.system_prompt}

USER

{task}
"""

        return self.router.ask(prompt)

    def python(self):
        return self.tools.get("python")

    def git(self):
        return self.tools.get("git")

    def shell(self):
        return self.tools.get("shell")

    def filesystem(self):
        return self.tools.get("filesystem")

    def assign_task(self, task):
        self.inbox.add(task)

    def work(self):

        task = self.inbox.next()

        if task is None:
            return "No pending tasks."

        task.status = "IN_PROGRESS"
        logger.info("Agent %s starting task %s", self.name, task.title)

        answer = self.run(task.description)

        task.status = "COMPLETED"
        logger.info("Agent %s completed task %s", self.name, task.title)

        return answer
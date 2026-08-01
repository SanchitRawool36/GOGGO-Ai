from runtime.agents.agent_manager import AgentManager
from runtime.tasks.task_manager import TaskManager


class Orchestrator:

    def __init__(self):

        self.agents = AgentManager()
        self.tasks = TaskManager()

    def assign(self, title, description, agent, priority="MEDIUM"):

        task = self.tasks.create_task(
            title=title,
            description=description,
            assigned_to=agent,
            priority=priority,
        )

        worker = self.agents.get(agent)

        worker.assign_task(task)

        return worker.work()
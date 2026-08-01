from runtime.core.logger import logger
from runtime.planner.planner import Planner
from runtime.tasks.task_manager import TaskManager
from runtime.collaboration.collaboration import Collaboration
from runtime.agents.agent_manager import AgentManager
from runtime.context.context_manager import ContextManager


class RuntimeEngine:

    def __init__(self):

        self.context = ContextManager()

        self.planner = Planner()

        self.task_manager = TaskManager()

        self.agent_manager = AgentManager()

        self.collaboration = Collaboration(
            self.agent_manager
        )

    def run(self, goal):

        logger.info("AI Runtime Started")
        logger.info("Goal: %s", goal)
        logger.info("Generating Plan")

        plan = self.planner.create_plan(goal)
        tasks = plan["tasks"]

        logger.info("%s tasks generated", len(tasks))

        for task in tasks:
            created = self.task_manager.create_task(
                title=task["title"],
                description=task["description"],
                assigned_to=task["agent"],
            )
            logger.info("Executing task: %s", created.title)
            self.collaboration.execute(created)

        logger.info("Runtime Finished")
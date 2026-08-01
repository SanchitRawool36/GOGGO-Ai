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

        print("=" * 70)
        print("AI Runtime Started")
        print("=" * 70)

        print("\nGoal:")
        print(goal)

        print("\nGenerating Plan...\n")

        plan = self.planner.create_plan(goal)

        tasks = plan["tasks"]

        print(f"{len(tasks)} Tasks Generated\n")

        for task in tasks:

            created = self.task_manager.create_task(

                title=task["title"],

                description=task["description"],

                assigned_to=task["agent"]

            )

            self.collaboration.execute(created)

        print("\nRuntime Finished.\n")
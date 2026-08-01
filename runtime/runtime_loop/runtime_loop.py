from runtime.planner.planner import Planner
from runtime.tasks.task_manager import TaskManager
from runtime.collaboration.collaboration import Collaboration
from runtime.agents.agent_manager import AgentManager


class RuntimeLoop:

    def __init__(self):
        self.planner = Planner()
        self.tasks = TaskManager()
        self.agents = AgentManager()
        self.collaboration = Collaboration(self.agents, self.tasks)

    def execute(self, goal):
        print("\n==============================")
        print("GOAL")
        print("==============================")
        print(goal)

        print("\nGenerating plan...\n")

        plan = self.planner.create_plan(goal)

        print("Plan Generated.\n")

        created_tasks = []

        for task in plan["tasks"]:
            new_task = self.tasks.create_task(
                title=task["title"],
                description=task["description"],
                assigned_to=task["agent"],
            )
            created_tasks.append(new_task)

        print(f"{len(created_tasks)} tasks created.\n")

        for task in created_tasks:
            print("=" * 60)
            print("Executing:", task.title)
            self.collaboration.execute(task)

        print("\nRuntime Finished.")
from runtime.planner.planner import Planner
from runtime.tasks.task_manager import TaskManager
from runtime.decision.decision_engine import DecisionEngine
from runtime.collaboration.collaboration import Collaboration


class AutonomousRuntime:

    def __init__(self):

        self.planner = Planner()

        self.tasks = TaskManager()

        self.decision = DecisionEngine()

        self.collaboration = Collaboration()

    def run(self, goal):

        print("=" * 70)
        print("AUTONOMOUS RUNTIME")
        print("=" * 70)

        print("\nGoal:")
        print(goal)

        print("\nGenerating Plan...")

        plan = self.planner.create_plan(goal)

        print("Done.")

        for item in plan["tasks"]:

            self.tasks.create_task(

                title=item["title"],

                description=item["description"],

                assigned_to=item["agent"]

            )

        all_tasks = self.tasks.list_tasks()

        print(f"\n{len(all_tasks)} Tasks Created")

        while self.decision.should_continue(all_tasks):

            pending = [

                t

                for t in all_tasks

                if t.status != "COMPLETED"

            ]

            if not pending:

                break

            task = pending[0]

            action = self.decision.decide(task)

            print("\n" + "=" * 60)

            print(task.title)

            print("Decision:", action)

            print("=" * 60)

            if action == "EXECUTE":

                self.collaboration.execute(task)

        print("\n")

        print("=" * 70)

        print("PROJECT COMPLETE")

        print("=" * 70)
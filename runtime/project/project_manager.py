from runtime.runtime_engine import RuntimeEngine


class ProjectManager:
    """
    High-level manager responsible for running
    complete AI projects.
    """

    def __init__(self):

        self.runtime = RuntimeEngine()

        self.projects = []

    # --------------------------------
    # Create Project
    # --------------------------------

    def create_project(self, goal: str):

        project = {
            "goal": goal,
            "status": "CREATED"
        }

        self.projects.append(project)

        return project

    # --------------------------------
    # Execute Project
    # --------------------------------

    def execute_project(self, goal: str):

        project = self.create_project(goal)

        print("=" * 70)
        print("PROJECT CREATED")
        print("=" * 70)

        print(f"Goal : {goal}")

        print()

        project["status"] = "RUNNING"

        self.runtime.run(goal)

        project["status"] = "COMPLETED"

        print()

        print("=" * 70)
        print("PROJECT COMPLETED")
        print("=" * 70)

        return project

    # --------------------------------
    # List Projects
    # --------------------------------

    def list_projects(self):

        return self.projects
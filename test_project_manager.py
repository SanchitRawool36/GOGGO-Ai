from runtime.project.project_manager import ProjectManager


manager = ProjectManager()

manager.execute_project(
    "Build a Hospital Management System"
)

print()

print("Saved Projects")

for project in manager.list_projects():

    print(project)
from runtime.tasks.task_manager import TaskManager

manager = TaskManager()

task = manager.create_task(
    title="Build Backend",
    description="Develop FastAPI backend APIs",
    assigned_to="CTO",
    priority="HIGH",
)

print(task)

print("\nAll Tasks:\n")

for task in manager.list_tasks():
    print(task)
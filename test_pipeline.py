from runtime.planner.planner import Planner
from runtime.tasks.task_manager import TaskManager
from runtime.orchestrator.orchestrator import Orchestrator

# Step 3: Create the objects
planner = Planner()
task_manager = TaskManager()
orchestrator = Orchestrator()

# Step 4: Give the system a real goal
goal = "Build Hospital Management System"

# Step 5: Generate a plan
print("Generating plan...")
plan = planner.create_plan(goal)
print("Plan generated.")

# Step 6: Convert the plan into runtime tasks
print("Creating tasks from plan...")
task_manager.create_from_plan(plan)
print("Tasks created.")

# Step 7: Display the generated tasks
print("\nGenerated Tasks:\n")
for task in task_manager.list_tasks():
    print(f"Title: {task.title}")
    print(f"Description: {task.description}")
    print(f"Assigned to: {task.assigned_to}")
    print(f"Status: {task.status}")
    print("-" * 20)

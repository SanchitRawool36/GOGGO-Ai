from runtime.collaboration.collaboration import Collaboration
from runtime.tasks.task_manager import TaskManager

# Initialize TaskManager. By default, it stores tasks in-memory.
task_manager = TaskManager()

# Create a new task for the collaboration workflow.
# This task will be passed through the multi-agent pipeline.
task = task_manager.create_task(
    title="Build Login API Endpoint",
    description="Create a secure JWT-based authentication endpoint using FastAPI. It should include token generation and validation.",
    assigned_to="CTO" # The initial agent assignment, though the workflow will manage assignments.
)

print(f"--- Starting Collaboration for Task: '{task.title}' ---")
print(f"Initial Task Status: {task.status}\\n")

# Initialize the Collaboration class and execute the workflow with the created task.
collab = Collaboration()
collab.execute(task)

print(f"\\n--- Collaboration Finished ---")
print(f"Final Task Status: {task.status}")

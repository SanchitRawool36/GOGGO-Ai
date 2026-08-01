from runtime.agents.agent_manager import AgentManager
from runtime.tasks.task_manager import TaskManager

agents = AgentManager()
tasks = TaskManager()

task = tasks.create_task(
    title="Backend API",
    description="Design the architecture of our FastAPI backend.",
    assigned_to="CTO",
    priority="HIGH",
)

cto = agents.get("cto")

cto.assign_task(task)

print("Pending:", cto.inbox.pending())

print()

answer = cto.work()

print(answer)

print()

print(task.status)
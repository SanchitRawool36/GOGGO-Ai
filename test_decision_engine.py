from runtime.decision.decision_engine import DecisionEngine
from runtime.tasks.task import Task

engine = DecisionEngine()

tasks = [

    Task(
        title="Backend",
        description="Build API",
        assigned_to="CTO"
    ),

    Task(
        title="Frontend",
        description="Build UI",
        assigned_to="CEO"
    )

]

tasks[0].status = "PENDING"

tasks[1].status = "COMPLETED"

print("=" * 60)

print("DECISIONS")

print("=" * 60)

for task in tasks:

    print(task.title)

    print(engine.decide(task))

    print()

print("=" * 60)

print("CONTINUE PROJECT")

print("=" * 60)

print(engine.should_continue(tasks))
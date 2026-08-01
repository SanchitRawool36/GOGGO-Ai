from runtime.planner.planner import Planner

planner = Planner()

plan = planner.create_plan(
    "Build Hospital Management System"
)

print(plan.goal)

for task in plan.tasks:
    print(task)
from runtime.orchestrator.orchestrator import Orchestrator

orchestrator = Orchestrator()

print("=" * 60)
print("CTO")
print("=" * 60)

backend = orchestrator.assign(
    title="Backend",
    description="Design a FastAPI backend architecture.",
    agent="cto",
    priority="HIGH",
)

print(backend)

print("\n")

print("=" * 60)
print("HR")
print("=" * 60)

hiring = orchestrator.assign(
    title="Hiring",
    description="Create the first hiring roadmap for engineers.",
    agent="hr",
)

print(hiring)

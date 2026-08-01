from runtime.agents.agent_manager import AgentManager

manager = AgentManager()

cto = manager.get_agent("CTO")

print("Testing Agent Tools...\n")

print("Python:", cto.python())
print("Git:", cto.git())
print("Shell:", cto.shell())
print("Filesystem:", cto.filesystem())

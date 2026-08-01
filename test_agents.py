from runtime.agents.agent_manager import AgentManager

manager = AgentManager()

ceo = manager.get("ceo")

print("\nCEO Thinking...\n")

answer = ceo.run(
    "We are building an AI operating system. What should our first milestone be?"
)

print(answer)
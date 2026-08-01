from runtime.agents.agent_manager import AgentManager
from runtime.prompts.tool_prompt import TOOL_SYSTEM_PROMPT
from runtime.tool_calling.tool_caller import ToolCaller

manager = AgentManager()

cto = manager.get("CTO")

prompt = TOOL_SYSTEM_PROMPT + """

Create a python file named hello_ai.py

that prints

Hello AI Company

"""

response = cto.run(prompt)

print("\nLLM RESPONSE\n")
print(response)

caller = ToolCaller()

try:

    result = caller.execute_json(response)

    print("\nTOOL RESULT\n")

    print(result)

except Exception as e:

    print("\nNot valid JSON\n")

    print(e)
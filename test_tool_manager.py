from runtime.tools.tool_manager import ToolManager

manager = ToolManager()

print("Available Tools:\n")

for tool in manager.list_tools():
    print("-", tool)
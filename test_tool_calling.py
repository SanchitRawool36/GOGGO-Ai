from runtime.tool_calling.tool_caller import ToolCaller

caller = ToolCaller()

request = {
    "tool": "filesystem",
    "action": "write_file",
    "args": {
        "path": "hello_tool.txt",
        "content": "Created by Tool Caller"
    }
}

result = caller.execute(request)

print("\nRESULT")
print(result)
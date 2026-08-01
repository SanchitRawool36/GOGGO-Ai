from runtime.executor.action_executor import ActionExecutor

executor = ActionExecutor()

code = """
print("Hello from AI Company")
"""

print(
    executor.execute_python(
        code,
        "hello_ai.py"
    )
)
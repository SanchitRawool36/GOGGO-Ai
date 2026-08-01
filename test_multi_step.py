from runtime.execution.multi_step_executor import MultiStepExecutor

executor = MultiStepExecutor()

steps = [
    {
        "tool": "filesystem",
        "action": "create_folder",
        "args": {
            "path": "demo_ai"
        }
    },
    {
        "tool": "filesystem",
        "action": "write_file",
        "args": {
            "path": "demo_ai/main.py",
            "content": "print('Hello AI Company')"
        }
    },
    {
        "tool": "python",
        "action": "run_file",
        "args": {
            "filename": "demo_ai/main.py"
        }
    }
]

executor.execute(steps)

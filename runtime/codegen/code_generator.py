from runtime.router.model_router import ModelRouter
from runtime.executor.action_executor import ActionExecutor


class CodeGenerator:

    def __init__(self):

        self.router = ModelRouter()
        self.executor = ActionExecutor()

    # ------------------------------------------------

    def generate_only(self, prompt: str):

        system = f"""
You are an expert Python software engineer.

Only return code.

No explanation.

No markdown.

No ```.

Task:

{prompt}
"""

        code = self.router.ask(system)

        code = code.replace("```python", "")
        code = code.replace("```", "")

        return code.strip()

    # ------------------------------------------------

    def generate_python(self, prompt, filename="generated_app.py"):

        code = self.generate_only(prompt)

        print(f"\nSaved -> {filename}")

        result = self.executor.execute_python(
            code,
            filename
        )

        return result
import traceback


class ErrorFixer:
    """
    Responsible for analysing Python errors
    and asking the AI to repair code.
    """

    def __init__(self, router):
        self.router = router

    def build_prompt(self, code: str, error: str) -> str:

        return f"""
You are an expert Python software engineer.

The following Python code produced an error.

Your task:

1. Fix the code.
2. Do NOT explain anything.
3. Return ONLY valid Python code.
4. No markdown.
5. No triple backticks.
6. Keep functionality the same.

ERROR:

{error}

CODE:

{code}

Return only corrected Python.
"""

    def fix(self, code: str, error: str):

        prompt = self.build_prompt(code, error)

        fixed = self.router.ask(prompt)

        fixed = fixed.replace("```python", "")
        fixed = fixed.replace("```", "")
        fixed = fixed.strip()

        return fixed
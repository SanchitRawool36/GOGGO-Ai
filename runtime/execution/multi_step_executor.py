import json

from runtime.tool_calling.tool_caller import ToolCaller


class MultiStepExecutor:

    def __init__(self):
        self.caller = ToolCaller()

    def execute(self, steps):

        results = []

        for i, step in enumerate(steps, start=1):

            print(f"\n========== STEP {i} ==========")

            result = self.caller.execute(step)

            print(result)

            results.append(result)

        return results

    def execute_json(self, response):

        data = json.loads(response)

        return self.execute(data["steps"])

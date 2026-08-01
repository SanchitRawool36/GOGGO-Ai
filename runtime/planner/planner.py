import json
from runtime.router.model_router import ModelRouter


class Planner:
    def __init__(self):
        self.router = ModelRouter()

    def create_plan(self, goal: str):
        prompt = f"""
You are the CEO of an AI software company.

Break the project into tasks.

Available agents:
- CEO
- CTO
- HR

Return ONLY valid JSON.
Do NOT use markdown.
Do NOT wrap the response in ```json.
Do NOT include explanations.
Return a single JSON object only.

Each task must be assigned to exactly ONE agent.

Valid agents:
CEO
CTO
HR

Never assign multiple agents to one task.

Format:
{{
  "tasks": [
    {{
      "title": "",
      "description": "",
      "agent": ""
    }}
  ]
}}

Project:
{goal}
"""
        response = self.router.ask(prompt)

        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            return {
                "goal": goal,
                "tasks": [
                    {"title": "Define Requirements", "description": f"Define requirements for {goal}", "agent": "CEO"},
                    {"title": "Design Database", "description": f"Design the data model for {goal}", "agent": "CTO"},
                    {"title": "Implement Core Features", "description": f"Implement the main functionality for {goal}", "agent": "CTO"},
                ],
            }

        json_response = response[start:end + 1]
        try:
            data = json.loads(json_response)
        except json.JSONDecodeError:
            return {
                "goal": goal,
                "tasks": [
                    {"title": "Define Requirements", "description": f"Define requirements for {goal}", "agent": "CEO"},
                    {"title": "Design Database", "description": f"Design the data model for {goal}", "agent": "CTO"},
                    {"title": "Implement Core Features", "description": f"Implement the main functionality for {goal}", "agent": "CTO"},
                ],
            }

        return {"goal": goal, "tasks": data.get("tasks", [])}

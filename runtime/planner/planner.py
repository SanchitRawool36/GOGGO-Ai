import json
from pydantic import BaseModel
from typing import List
from runtime.router.model_router import ModelRouter

class PlannedTask(BaseModel):
    title: str
    description: str
    agent: str

class ProjectPlan(BaseModel):
    goal: str
    tasks: List[PlannedTask]

class Planner:
    def __init__(self):
        self.router = ModelRouter()

    def create_plan(self, goal: str) -> ProjectPlan:
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
 "tasks":[
   {{
      "title":"",
      "description":"",
      "agent":""
   }}
 ]
}}

Project:
{goal}
"""
        response = self.router.ask(prompt)
        
        # Find the start and end of the JSON object
        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON object found in the response")

        json_response = response[start:end + 1]
        
        try:
            data = json.loads(json_response)
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")
            print(f"Response was: {json_response}")
            raise

        tasks = [
            PlannedTask(**task)
            for task in data["tasks"]
        ]

        return ProjectPlan(
            goal=goal,
            tasks=tasks,
        )

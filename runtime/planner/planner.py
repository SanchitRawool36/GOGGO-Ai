import json
from typing import Any, Dict, List

from runtime.router.model_router import ModelRouter


class Planner:
    """Create structured plans with richer task metadata for the runtime."""

    def __init__(self) -> None:
        self.router = ModelRouter()

    def create_plan(self, goal: str) -> Dict[str, Any]:
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
      "agent": "",
      "priority": "MEDIUM",
      "required_tools": []
    }}
  ]
}}

Project:
{goal}
"""
        response = self.router.ask(prompt)
        start = response.find("{")
        end = response.rfind("}")

        fallback_tasks = [
            {
                "title": "Define Requirements",
                "description": f"Define requirements for {goal}",
                "agent": "CEO",
                "priority": "HIGH",
                "required_tools": ["filesystem"],
            },
            {
                "title": "Design Database",
                "description": f"Design the data model for {goal}",
                "agent": "CTO",
                "priority": "HIGH",
                "required_tools": ["filesystem"],
            },
            {
                "title": "Implement Core Features",
                "description": f"Implement the main functionality for {goal}",
                "agent": "CTO",
                "priority": "MEDIUM",
                "required_tools": ["python"],
            },
        ]

        if start == -1 or end == -1:
            return {"goal": goal, "tasks": fallback_tasks}

        json_response = response[start:end + 1]
        try:
            data = json.loads(json_response)
        except json.JSONDecodeError:
            return {"goal": goal, "tasks": fallback_tasks}

        tasks = data.get("tasks", [])
        if not isinstance(tasks, list):
            return {"goal": goal, "tasks": fallback_tasks}
        return {"goal": goal, "tasks": self._normalize_tasks(tasks)}

    def _normalize_tasks(self, tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        normalized: List[Dict[str, Any]] = []
        for index, task in enumerate(tasks):
            normalized.append(
                {
                    "title": task.get("title", f"Task {index + 1}"),
                    "description": task.get("description", ""),
                    "agent": task.get("agent", "CTO"),
                    "priority": task.get("priority", "MEDIUM"),
                    "required_tools": task.get("required_tools", []),
                    "status": "PENDING",
                    "dependencies": [],
                    "retry_count": 0,
                    "execution_order": index,
                }
            )
        return normalized

from runtime.agents.base_agent import BaseAgent
from runtime.prompts.system_prompts import (
    CEO_PROMPT,
    CTO_PROMPT,
    HR_PROMPT,
)


class AgentManager:

    def __init__(self):

        self.agents = {
            "ceo": BaseAgent(
                "CEO",
                "Chief Executive Officer",
                CEO_PROMPT,
            ),

            "cto": BaseAgent(
                "CTO",
                "Chief Technology Officer",
                CTO_PROMPT,
            ),

            "hr": BaseAgent(
                "HR",
                "Human Resources",
                HR_PROMPT,
            ),
        }

    def get(self, name: str):

        return self.agents[name.lower()]

    def delegate(self, agent_name: str, task: str):
        agent = self.get(agent_name)
        return agent.run(task)
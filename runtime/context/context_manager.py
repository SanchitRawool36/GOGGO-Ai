from datetime import datetime


class ContextManager:

    def __init__(self):

        self.project = None
        self.history = []
        self.current_agent = None

    def set_project(self, project_name):

        self.project = project_name

    def set_agent(self, agent):

        self.current_agent = agent

    def add_history(self, role, message):

        self.history.append(
            {
                "time": datetime.now(),
                "role": role,
                "message": message,
            }
        )

    def recent(self, limit=5):

        return self.history[-limit:]

    def build_context(self):

        return {
            "project": self.project,
            "agent": self.current_agent,
            "history": self.recent(),
        }
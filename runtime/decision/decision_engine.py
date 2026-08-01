class DecisionEngine:
    """
    Simple rule-based decision engine.

    Later this will become LLM-powered.
    """

    def decide(self, task):

        status = task.status.upper()

        if status == "PENDING":
            return "EXECUTE"

        if status == "FAILED":
            return "RETRY"

        if status == "REVIEW":
            return "CEO_REVIEW"

        if status == "COMPLETED":
            return "NEXT_TASK"

        return "UNKNOWN"

    def should_continue(self, tasks):

        for task in tasks:

            if task.status != "COMPLETED":
                return True

        return False
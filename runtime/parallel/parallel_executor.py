from concurrent.futures import ThreadPoolExecutor, as_completed

from runtime.agents.agent_manager import AgentManager


class ParallelExecutor:
    """
    Runs multiple AI agents in parallel.
    """

    def __init__(self):
        self.manager = AgentManager()

    def _run_agent(self, agent_name: str, prompt: str):

        agent = self.manager.get(agent_name)

        result = agent.run(prompt)

        return {
            "agent": agent_name,
            "result": result
        }

    def execute(self, jobs):

        results = []

        with ThreadPoolExecutor(max_workers=len(jobs)) as executor:

            futures = [
                executor.submit(
                    self._run_agent,
                    job["agent"],
                    job["prompt"]
                )
                for job in jobs
            ]

            for future in as_completed(futures):

                results.append(future.result())

        return results
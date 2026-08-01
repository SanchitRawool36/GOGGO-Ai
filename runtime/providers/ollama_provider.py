from __future__ import annotations

from runtime.core.config import config

try:
    from ollama import Client
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    Client = None


class OllamaProvider:

    def __init__(self, model):
        self.model = model
        self.client = Client(host=config.ollama_host) if Client is not None else None

    def chat(self, prompt: str):
        if self.client is None:
            return f"OllamaProvider placeholder for {self.model}: {prompt[:80]}"

        response = self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]
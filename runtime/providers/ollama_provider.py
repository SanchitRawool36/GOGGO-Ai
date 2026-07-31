from ollama import Client

from runtime.core.config import config


class OllamaProvider:
    def __init__(self):
        self.client = Client(host=config.ollama_host)

    def chat(self, prompt: str, model: str | None = None):

        response = self.client.chat(
            model=model or config.default_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]


ollama_provider = OllamaProvider()
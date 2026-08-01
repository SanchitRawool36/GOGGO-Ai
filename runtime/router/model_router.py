from __future__ import annotations

from runtime.core.config import config

try:
    from runtime.providers.ollama_provider import OllamaProvider
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    OllamaProvider = None


class ModelRouter:

    def __init__(self, model=None):
        self.model = model or config.default_model
        self.ollama = OllamaProvider(self.model) if OllamaProvider is not None else None

    def ask(self, prompt: str):
        if self.ollama is None:
            return f"ModelRouter placeholder for {self.model}: {prompt[:80]}"
        return self.ollama.chat(prompt)
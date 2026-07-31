from runtime.providers.ollama_provider import ollama_provider


class ModelRouter:

    def ask(
        self,
        prompt: str,
        use_cloud: bool = False,
    ):

        if use_cloud:
            raise NotImplementedError(
                "Cloud provider not implemented yet."
            )

        return ollama_provider.chat(prompt)


router = ModelRouter()
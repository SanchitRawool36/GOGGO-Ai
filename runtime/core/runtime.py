from runtime.core.logger import logger
from runtime.core.config import config


class Runtime:

    def __init__(self):

        logger.info("Starting GOGGO Runtime")

        self.config = config

        logger.info(
            f"Model: {self.config.default_model}"
        )

        logger.info(
            f"Ollama: {self.config.ollama_host}"
        )


runtime = Runtime()
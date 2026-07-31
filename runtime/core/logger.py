import logging
from rich.logging import RichHandler


def setup_logger():

    logging.basicConfig(
        level="INFO",
        format="%(message)s",
        handlers=[
            RichHandler(
                rich_tracebacks=True
            )
        ],
    )

    return logging.getLogger("GOGGO")


logger = setup_logger()
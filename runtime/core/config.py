from pathlib import Path
from pydantic import BaseModel


class RuntimeConfig(BaseModel):
    app_name: str = "GOGGO-AI"
    version: str = "0.1.0"

    root_dir: Path = Path.cwd()

    agents_dir: Path = Path("agents")
    memory_dir: Path = Path("memory")
    configs_dir: Path = Path("configs")
    runtime_dir: Path = Path("runtime")

    default_model: str = "qwen2.5-coder:3b"

    ollama_host: str = "http://127.0.0.1:11434"

    log_level: str = "INFO"


config = RuntimeConfig()
from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Union


PathLike = Union[str, Path]


@dataclass
class ShellResult:
    command: str
    returncode: int
    stdout: str
    stderr: str


class ShellTool:
    """Small wrapper around subprocess for shell commands."""

    def run(
        self,
        command: str,
        timeout: Optional[int] = None,
        cwd: Optional[PathLike] = None,
    ) -> ShellResult:
        completed = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(cwd) if cwd is not None else None,
        )
        return ShellResult(
            command=command,
            returncode=completed.returncode,
            stdout=completed.stdout,
            stderr=completed.stderr,
        )
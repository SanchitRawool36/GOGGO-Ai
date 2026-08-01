import subprocess
from pathlib import Path
from typing import Iterable, Optional, Union


PathLike = Union[str, Path]


def _run_git_command(repo_path: PathLike, args: Iterable[str]) -> str:
    """Run a git command in the given repository and return its output."""
    repo = Path(repo_path)
    command = ["git", "-C", str(repo), *list(args)]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        details = result.stderr.strip() or result.stdout.strip() or "unknown git error"
        raise RuntimeError(details)

    return result.stdout.strip()


def status(repo_path: PathLike = ".") -> str:
    """Return the git status for the repository."""
    return _run_git_command(repo_path, ["status", "--short", "--branch"])


def add(repo_path: PathLike = ".", files: Optional[Iterable[str]] = None) -> str:
    """Stage files or the whole repository if no files are provided."""
    args = ["add"]
    if files:
        args.extend(list(files))
    else:
        args.append(".")
    return _run_git_command(repo_path, args)


def commit(repo_path: PathLike = ".", message: str = "chore: update") -> str:
    """Create a git commit with the provided message."""
    return _run_git_command(repo_path, ["commit", "-m", message])


def push(repo_path: PathLike = ".") -> str:
    """Push the current branch to the configured remote."""
    return _run_git_command(repo_path, ["push"])

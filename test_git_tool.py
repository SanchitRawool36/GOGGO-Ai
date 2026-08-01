import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "runtime" / "tools"))

from git_tool import add, commit, push, status


def main() -> None:
    print("Running git tool smoke test...")
    print("Status:", status())
    print("Add:", add(files=["runtime/tools/git_tool.py"]))
    print("Commit:", commit(message="chore: add git tool"))
    print("Push:", push())


if __name__ == "__main__":
    main()

from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent / "runtime" / "tools"))

from python_runner import run_demo


def main() -> None:
    print("Running Python runner smoke test...")
    result = run_demo()
    print(result)
    assert "PythonRunner" in result


if __name__ == "__main__":
    main()

from pathlib import Path

from runtime.repository.parser import RepositoryParser


IGNORE = {
    ".venv",
    "__pycache__",
    ".git",
    "memory_db",
    "dashboard",
    "docs",
    "docker",
    "scripts",
    "tests",
    "demo_ai",
    "demo_project",
}


class SymbolIndex:

    def __init__(self):

        self.parser = RepositoryParser()

        self.symbols = {}

    def build(self, root="."):

        self.symbols = {}

        count = 0
        files = list(Path(root).rglob("*.py"))

        print(f"Found {len(files)} python files")

        for i, file in enumerate(files, 1):

            if any(part in IGNORE for part in file.parts):
                continue

            print(f"[{i}/{len(files)}] {file}")
            print("Parsing:", file)

            try:

                info = self.parser.parse(file)

                count += 1

                for cls in info["classes"]:

                    self.symbols[cls] = {
                        "type": "class",
                        "file": str(file),
                    }

                for fn in info["functions"]:

                    self.symbols[fn] = {
                        "type": "function",
                        "file": str(file),
                    }

            except Exception as e:

                print("ERROR:", file)
                print(e)

        print("\nParsed", count, "Python files")

        return self.symbols

    def find(self, name):

        return self.symbols.get(name)

    def all(self):

        return self.symbols

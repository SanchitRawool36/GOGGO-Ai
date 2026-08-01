from pathlib import Path

IGNORE = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    "memory_db",
    "D:AI-CompanyModelsOllama",
    "docker",
}


class ProjectScanner:

    def scan(self, folder="."):

        folder = Path(folder)
        project = []

        for current in folder.iterdir():

            if current.name in IGNORE:
                continue

            print(f"\n===== Scanning {current} =====")

            try:
                count = 0

                for file in current.rglob("*"):

                    if any(part in IGNORE for part in file.parts):
                        continue

                    count += 1

                    if count % 100 == 0:
                        print(f"{current.name}: {count}")

                    if file.is_file():
                        project.append(
                            {
                                "name": file.name,
                                "path": str(file),
                                "extension": file.suffix,
                                "size": file.stat().st_size,
                            }
                        )

                print(f"Finished {current.name}")

            except Exception as e:
                print(f"ERROR in {current}: {e}")

        return project

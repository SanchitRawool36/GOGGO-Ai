from __future__ import annotations

import json
import os
import traceback
from pathlib import Path
from typing import Any, Dict, List, Optional

from runtime.repository.parser import RepositoryParser


IGNORE = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    "memory_db",
    "dist",
    "build",
    ".idea",
    ".vscode",
}


class RepositoryIndex:
    """Repository-wide symbol index for AI understanding."""

    def __init__(
        self,
        root: str = ".",
        cache_path: Optional[str] = None,
    ):

        self.root = Path(root)
        self.cache_path = Path(cache_path) if cache_path else None

        self.parser = RepositoryParser()

        self.index: Dict[str, Dict[str, Any]] = {}
        self.files: Dict[str, Dict[str, Any]] = {}
        self.modules: Dict[str, Dict[str, Any]] = {}

    # --------------------------------------------------

    def build(self):

        print("\nBuilding Repository Index...\n")

        self.index.clear()
        self.files.clear()
        self.modules.clear()

        python_files = []

        # Safe recursive scan
        for root, dirs, files in os.walk(self.root):

            dirs[:] = [
                d for d in dirs
                if d not in IGNORE
            ]

            for file in files:

                if file.endswith(".py"):

                    python_files.append(
                        Path(root) / file
                    )

        total = len(python_files)

        print(f"Found {total} Python files\n")

        parsed = 0

        for i, path in enumerate(sorted(python_files), start=1):

            rel_path = path.as_posix()

            print(f"[{i}/{total}] Parsing {rel_path}")

            try:

                info = self.parser.parse(path)

                self.files[rel_path] = {
                    "path": rel_path,
                    "classes": info.get("classes", []),
                    "functions": info.get("functions", []),
                    "imports": info.get("imports", []),
                    "calls": info.get("calls", []),
                }

                self.modules[rel_path] = {
                    "path": rel_path
                }

                for cls in info.get("classes", []):
                    self.index[f"class:{cls}"] = {
                        "type": "class",
                        "file": rel_path,
                    }

                for fn in info.get("functions", []):

                    self.index[f"function:{fn}"] = {
                        "type": "function",
                        "file": rel_path,
                    }

                for imp in info.get("imports", []):

                    self.index[f"import:{imp}"] = {
                        "type": "import",
                        "file": rel_path,
                    }

                parsed += 1

                print("   ✓ OK")

            except Exception as e:

                print(f"   ✗ ERROR : {e}")

                traceback.print_exc()

        print("\n========================================")
        print("Repository Index Complete")
        print("========================================")
        print("Files Parsed :", parsed)
        print("Files Indexed:", len(self.files))
        print("Modules      :", len(self.modules))
        print("Symbols      :", len(self.index))

        self._cache()

        return self.index

    # --------------------------------------------------

    def find_class(self, name: str):

        return self.index.get(f"class:{name}")

    def find_function(self, name: str):

        return self.index.get(f"function:{name}")

    def find_method(self, name: str):

        return self.index.get(f"method:{name}")

    def find_file(self, filename: str):

        return self.files.get(filename)

    def find_import(self, name: str):

        return self.index.get(f"import:{name}")

    # --------------------------------------------------

    def search(self, keyword: str):

        keyword = keyword.lower()

        results = []

        for key, value in self.index.items():

            if keyword in key.lower():

                results.append(
                    {
                        "key": key,
                        **value,
                    }
                )

        return results

    # --------------------------------------------------

    def get_index(self):

        return self.index

    def get_files(self):

        return self.files

    def get_modules(self):

        return self.modules

    # --------------------------------------------------

    def _cache(self):

        if self.cache_path is None:
            return

        self.cache_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.cache_path.write_text(
            json.dumps(
                self.index,
                indent=2,
            ),
            encoding="utf-8",
        )
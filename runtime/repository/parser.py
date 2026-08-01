import ast
from pathlib import Path


class RepositoryParser:

    def parse(self, filename):

        filename = Path(filename)

        source = filename.read_text(encoding="utf-8")

        tree = ast.parse(source)

        info = {
            "file": str(filename),
            "classes": [],
            "functions": [],
            "imports": [],
            "calls": [],
        }

        for node in ast.walk(tree):

            if isinstance(node, ast.ClassDef):
                info["classes"].append(node.name)

            elif isinstance(node, ast.FunctionDef):
                info["functions"].append(node.name)

            elif isinstance(node, ast.Import):
                for name in node.names:
                    info["imports"].append(name.name)

            elif isinstance(node, ast.ImportFrom):
                module = node.module or ""
                info["imports"].append(module)

            elif isinstance(node, ast.Call):

                if isinstance(node.func, ast.Name):
                    info["calls"].append(node.func.id)

                elif isinstance(node.func, ast.Attribute):
                    info["calls"].append(node.func.attr)

        return info

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple


class DependencyGraph:
    """Build a lightweight import dependency graph for the repository."""

    def __init__(self, root: str = ".") -> None:
        self.root = Path(root)
        self.graph: Dict[str, Set[str]] = {}
        self.reverse_graph: Dict[str, Set[str]] = {}

    def build(self) -> Dict[str, Set[str]]:
        self.graph = {}
        self.reverse_graph = {}
        for path in sorted(self.root.rglob("*.py")):
            if self._should_ignore(path):
                continue
            module = self._module_name(path)
            imports = self._read_imports(path)
            self.graph[module] = set(imports)
            for dep in imports:
                self.reverse_graph.setdefault(dep, set()).add(module)
            self.reverse_graph.setdefault(module, set())
        return self.graph

    def get_graph(self) -> Dict[str, Set[str]]:
        return self.graph

    def get_reverse_imports(self, module: str) -> Set[str]:
        return self.reverse_graph.get(module, set())

    def detect_circular_dependencies(self) -> List[List[str]]:
        visited: Set[str] = set()
        stack: List[str] = []
        cycles: List[List[str]] = []

        def visit(node: str) -> None:
            visited.add(node)
            stack.append(node)
            for dep in self.graph.get(node, set()):
                if dep not in visited:
                    visit(dep)
                elif dep in stack:
                    cycle_start = stack.index(dep)
                    cycles.append(stack[cycle_start:] + [dep])
            stack.pop()

        for node in self.graph:
            if node not in visited:
                visit(node)
        return cycles

    def export_json(self) -> str:
        return json.dumps({"graph": self.graph, "reverse": self.reverse_graph}, indent=2)

    def print_graph(self) -> None:
        for module, deps in sorted(self.graph.items()):
            if deps:
                print(f"{module} -> {', '.join(sorted(deps))}")

    def _read_imports(self, path: Path) -> List[str]:
        imports: List[str] = []
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("from "):
                parts = line.split()
                if len(parts) >= 2:
                    imports.append(parts[1].split(".")[0])
            elif line.startswith("import "):
                parts = line.split()
                if len(parts) >= 2:
                    imports.append(parts[1].split(".")[0])
        return imports

    def _module_name(self, path: Path) -> str:
        return str(path).replace("\\", "/")

    def _should_ignore(self, path: Path) -> bool:
        ignore_parts = {".git", ".venv", "node_modules", "__pycache__", "memory_db", "dist", "build"}
        return any(part in ignore_parts for part in path.parts)

from __future__ import annotations

from typing import Any, Dict, List

from runtime.analyzer.project_scanner import ProjectScanner
from runtime.repository.dependency_graph import DependencyGraph
from runtime.repository.parser import RepositoryParser
from runtime.repository.repository_index import RepositoryIndex
from runtime.repository.symbol_index import SymbolIndex


class ProjectUnderstanding:
    """Aggregate repository intelligence into a usable project view."""

    def __init__(self, root: str = ".") -> None:
        self.root = root
        self.index = RepositoryIndex(root=root)
        self.graph = DependencyGraph(root=root)
        self.scanner = ProjectScanner()
        self.parser = RepositoryParser()
        self.symbols = SymbolIndex()

    def build(self) -> Dict[str, Any]:
        self.index.build()
        self.graph.build()
        self.symbols.build(self.root)
        files = self.scanner.scan(self.root)
        entry_points = self._find_entry_points(files)
        return {
            "project_summary": self._project_summary(files),
            "architecture_summary": self._architecture_summary(),
            "important_files": self._important_files(files),
            "important_classes": self._important_classes(),
            "important_functions": self._important_functions(),
            "project_tree": self._project_tree(files),
            "technology_stack": self._technology_stack(files),
            "dependency_overview": {"graph": self.graph.get_graph()},
            "execution_entry_points": entry_points,
        }

    def _project_summary(self, files: List[Dict[str, Any]]) -> str:
        py_files = sum(1 for item in files if item["extension"] == ".py")
        return f"Repository with {py_files} Python files and {len(files)} discovered files."

    def _architecture_summary(self) -> str:
        return "Runtime-oriented Python architecture with planner, task, agent, repository, and tool layers."

    def _important_files(self, files: List[Dict[str, Any]]) -> List[str]:
        candidates = [item["path"] for item in files if item["path"].endswith(("runtime_engine.py", "planner.py", "task.py", "symbol_index.py", "project_builder.py"))]
        return sorted(candidates)

    def _important_classes(self) -> List[str]:
        return [name for name in self.symbols.all().keys() if self.symbols.all()[name]["type"] == "class"]

    def _important_functions(self) -> List[str]:
        return [name for name in self.symbols.all().keys() if self.symbols.all()[name]["type"] == "function"]

    def _project_tree(self, files: List[Dict[str, Any]]) -> List[str]:
        return [item["path"] for item in files[:20]]

    def _technology_stack(self, files: List[Dict[str, Any]]) -> List[str]:
        stack = set()
        for item in files:
            if item["extension"] in {".py", ".md", ".yml", ".yaml", ".toml", ".txt"}:
                stack.add(item["extension"])
        return sorted(stack)

    def _find_entry_points(self, files: List[Dict[str, Any]]) -> List[str]:
        entry_points = []
        for item in files:
            if item["name"].startswith("main") or item["name"].endswith("_engine.py") or item["name"].endswith("runtime.py"):
                entry_points.append(item["path"])
        return entry_points

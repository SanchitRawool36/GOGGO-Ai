from pathlib import Path

from runtime.repository.repository_index import RepositoryIndex
from runtime.repository.dependency_graph import DependencyGraph
from runtime.repository.project_understanding import ProjectUnderstanding
from runtime.tasks.task_manager import TaskManager
from runtime.memory.agent_memory import AgentMemory


def test_repository_index_builds_core_symbols():
    index = RepositoryIndex(root="runtime")
    index.build()

    assert index.find_class("RuntimeEngine") is not None
    assert index.find_function("execute_python") is not None
    assert index.find_file("runtime/runtime_engine.py") is not None


def test_dependency_graph_detects_imports_and_cycles():
    graph = DependencyGraph(root="runtime")
    graph.build()

    assert graph.get_graph()
    assert graph.export_json() is not None
    assert isinstance(graph.detect_circular_dependencies(), list)


def test_project_understanding_generates_summary():
    understanding = ProjectUnderstanding(root="runtime")
    summary = understanding.build()

    assert summary["project_summary"]
    assert summary["architecture_summary"]
    assert summary["execution_entry_points"]


def test_task_manager_supports_lifecycle_and_execution():
    manager = TaskManager()
    task = manager.create_task(
        title="Inspect runtime",
        description="Inspect runtime modules",
        assigned_to="CTO",
        priority="HIGH",
    )

    assert task.id
    assert manager.read_task(task.id) is task

    updated = manager.modify_task(task.id, priority="LOW")
    assert updated.priority == "LOW"

    renamed = manager.rename_task(task.id, "Inspect runtime v2")
    assert renamed.title == "Inspect runtime v2"

    result = task.execute_shell("python --version")
    assert result["success"] is True

    manager.delete_task(task.id)
    assert manager.read_task(task.id) is None


def test_agent_memory_persists_and_summarizes():
    memory = AgentMemory("demo")
    memory.remember("lesson", "Keep tasks small")
    assert memory.latest(1)[0]["value"] == "Keep tasks small"
    summary = memory.summarize()
    assert summary["entry_count"] >= 1

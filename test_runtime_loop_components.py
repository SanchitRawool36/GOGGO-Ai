from runtime.runtime_loop.runtime_loop import RuntimeLoop
from runtime.tools.tool_manager import ToolManager
from runtime.tools.shell import ShellTool
from runtime.prompts.system_prompts import load_prompt


def test_runtime_loop_and_tools_are_available():
    loop = RuntimeLoop()
    assert loop is not None

    manager = ToolManager()
    assert manager is not None

    shell = ShellTool()
    result = shell.run("python -c \"print('ok')\"", timeout=10)
    assert result.returncode == 0
    assert "ok" in result.stdout

    prompt = load_prompt("ceo")
    assert "CEO" in prompt.upper()

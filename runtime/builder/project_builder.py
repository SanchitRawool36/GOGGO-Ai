from pathlib import Path
from typing import Dict, List

from runtime.codegen.code_generator import CodeGenerator
from runtime.executor.action_executor import ActionExecutor


class ProjectBuilder:
    """Create a simple project skeleton from a natural-language prompt."""

    def __init__(self) -> None:
        self.generator = CodeGenerator()
        self.executor = ActionExecutor()

    def build_file(self, filename: str, prompt: str) -> Dict[str, object]:
        print("\nGenerating Code...")
        code = self.generator.generate_only(prompt)

        print("Saving...")
        self.executor.tools.get("filesystem").write_file(filename, code)

        print("Running...")
        return self.executor.tools.get("python").run_file(filename)

    def scaffold(self, prompt: str, project_name: str = "generated_app") -> Dict[str, object]:
        files = {
            f"{project_name}/README.md": f"# {project_name}\n\nGenerated from: {prompt}\n",
            f"{project_name}/requirements.txt": "",
            f"{project_name}/main.py": "print('Hello from generated project')\n",
        }
        for path, content in files.items():
            self.executor.tools.get("filesystem").write_file(path, content)
        return {"project_name": project_name, "files": list(files.keys())}

    def build_project(self, prompt: str) -> Dict[str, object]:
        result = self.scaffold(prompt)
        project_name = result["project_name"]
        return {"project_name": project_name, "result": result}

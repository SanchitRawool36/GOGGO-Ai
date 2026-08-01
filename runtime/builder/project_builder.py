from runtime.codegen.code_generator import CodeGenerator
from runtime.executor.action_executor import ActionExecutor


class ProjectBuilder:

    def __init__(self):

        self.generator = CodeGenerator()

        self.executor = ActionExecutor()

    def build_file(self,
                   filename,
                   prompt):

        print("\nGenerating Code...")

        code = self.generator.generate_only(prompt)

        print("Saving...")

        self.executor.tools.get("filesystem").write_file(
            filename,
            code
        )

        print("Running...")

        result = self.executor.tools.get("python").run_file(filename)

        return result
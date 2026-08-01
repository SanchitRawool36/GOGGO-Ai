from runtime.codegen.code_generator import CodeGenerator

generator = CodeGenerator()

generator.generate_python(

    requirement="Create a calculator with add subtract multiply divide",

    filename="generated_calculator.py"

)

print("Done")
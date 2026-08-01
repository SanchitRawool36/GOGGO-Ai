from runtime.codegen.code_generator import CodeGenerator

generator = CodeGenerator()

result = generator.generate_python(

    "generated_app.py",

    "Create a Python program that prints Hello AI Company"

)

print()

print("=" * 60)

print("EXECUTION RESULT")

print("=" * 60)

print(result)
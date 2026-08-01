from runtime.builder.project_builder import ProjectBuilder

builder = ProjectBuilder()

result = builder.build_file(

    "calculator.py",

    """
Create a Python calculator.

Functions:

+

-

*

/

Take input from user.

Keep running until user types exit.
"""

)

print()

print("="*60)

print(result)
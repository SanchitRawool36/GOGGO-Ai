from runtime.context.context_manager import ContextManager

ctx = ContextManager()

ctx.set_project("Hospital Management System")

ctx.set_agent("CTO")

ctx.add_history(
    "user",
    "Create authentication module."
)

ctx.add_history(
    "cto",
    "Authentication module completed."
)

ctx.add_history(
    "user",
    "Now build patient management."
)

print(ctx.build_context())
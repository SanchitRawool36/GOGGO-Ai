from runtime.router.model_router import router

print()
print("Thinking...\n")

answer = router.ask(
    "Say hello in exactly five words."
)

print(answer)
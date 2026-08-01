from runtime.reflection.reflection_engine import ReflectionEngine


reflection = ReflectionEngine()


reflection.remember(
    task="Calculator",
    error="ZeroDivisionError",
    solution="Check denominator before division.",
)

reflection.remember(
    task="Login API",
    error="401 Unauthorized",
    solution="Verify JWT token before processing request.",
)

print("=" * 60)
print("ALL LESSONS")
print("=" * 60)

for lesson in reflection.show_all():

    print(lesson)

print()

print("=" * 60)
print("SEARCH: division")
print("=" * 60)

results = reflection.search("division")

for lesson in results:

    print(lesson)

print()

print("Total Lessons:", reflection.count())
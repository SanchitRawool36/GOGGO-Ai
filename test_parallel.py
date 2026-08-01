from runtime.parallel.parallel_executor import ParallelExecutor

parallel = ParallelExecutor()

jobs = [

    {
        "agent": "CEO",
        "prompt": "Give project vision for an AI Hospital Management System."
    },

    {
        "agent": "CTO",
        "prompt": "Design backend architecture for an AI Hospital Management System."
    },

    {
        "agent": "HR",
        "prompt": "Prepare hiring roadmap for AI Hospital Management System."
    }

]

results = parallel.execute(jobs)

print("\n" + "=" * 70)

print("PARALLEL EXECUTION RESULTS")

print("=" * 70)

for item in results:

    print(f"\nAgent : {item['agent']}")
    print("-" * 50)
    print(item["result"])
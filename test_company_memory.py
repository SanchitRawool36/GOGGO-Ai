from runtime.company.company_memory import CompanyMemory

memory = CompanyMemory()

memory.add(

    "CEO",

    "Requirement",

    "Hospital system must support patient registration."

)

memory.add(

    "CTO",

    "Architecture",

    "Backend will use FastAPI."

)

memory.add(

    "HR",

    "Hiring",

    "Need one Backend Developer."

)

print("=" * 60)

print("ALL KNOWLEDGE")

print("=" * 60)

for item in memory.all():

    print(item)

print()

print("=" * 60)

print("SEARCH : backend")

print("=" * 60)

for item in memory.search("backend"):

    print(item)

print()

print("=" * 60)

print("LATEST")

print("=" * 60)

for item in memory.latest():

    print(item)
from runtime.repository.parser import RepositoryParser

parser = RepositoryParser()

result = parser.parse("runtime/runtime_engine.py")

print()
print("=" * 60)
print("REPOSITORY PARSER")
print("=" * 60)

for k, v in result.items():

    print(k)

    print(v)

    print()

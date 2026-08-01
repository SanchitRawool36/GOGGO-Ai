from runtime.repository.repository_index import RepositoryIndex

print("=" * 60)
print("REPOSITORY INDEX")
print("=" * 60)

index = RepositoryIndex(".")
index.build()

print("\nTotal files indexed:")
print(len(index.files))

print("\nRuntimeEngine")
print(index.find_class("RuntimeEngine"))

print("\nToolManager")
print(index.find_class("ToolManager"))

print("\nexecute_python")
print(index.find_function("execute_python"))

print("\nSearch 'planner'")
print(index.search("planner"))
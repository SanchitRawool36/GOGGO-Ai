from runtime.repository.symbol_index import SymbolIndex

index = SymbolIndex()

index.build("runtime")

print()
print("=" * 60)
print("TOTAL SYMBOLS")
print("=" * 60)

print(len(index.all()))

print()
print("=" * 60)
print("RuntimeEngine")
print("=" * 60)

print(index.find("RuntimeEngine"))

print()
print("=" * 60)
print("ToolManager")
print("=" * 60)

print(index.find("ToolManager"))

print()
print("=" * 60)
print("execute_python")
print("=" * 60)

print(index.find("execute_python"))

from runtime.workspace.workspace_manager import WorkspaceManager

ws = WorkspaceManager("demo_project")

print("=" * 60)
print("CREATING PROJECT")
print("=" * 60)

ws.create_folder("backend")
ws.create_folder("frontend")
ws.create_folder("docs")

ws.create_file(
    "backend/main.py",
    "print('Backend Started')"
)

ws.create_file(
    "frontend/app.js",
    "console.log('Frontend Started');"
)

ws.create_file(
    "README.md",
    "# Demo Project"
)

print()

print("=" * 60)
print("TREE")
print("=" * 60)

for item in ws.tree():
    print(item)

print()

print("=" * 60)
print("SEARCH main")
print("=" * 60)

print(ws.search("main"))

print()

print("=" * 60)
print("READ FILE")
print("=" * 60)

print(ws.read_file("backend/main.py"))
from runtime.analyzer.project_scanner import ProjectScanner

scanner = ProjectScanner()

print("=" * 60)
print("PROJECT SCAN")
print("=" * 60)

files = scanner.scan(".")

print(f"\nFound {len(files)} files.\n")

print("First 20 files:\n")

for file in files[:20]:
    print(file)

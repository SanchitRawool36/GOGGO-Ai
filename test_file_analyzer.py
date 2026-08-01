from runtime.analyzer.file_analyzer import FileAnalyzer

analyzer = FileAnalyzer()

result = analyzer.analyze("generated_app.py")

print()
print("=" * 60)
print("FILE ANALYSIS")
print("=" * 60)

for k, v in result.items():

    if k != "content":
        print(k, ":", v)

from pathlib import Path


class FileAnalyzer:

    def analyze(self, path):

        path = Path(path)

        if not path.exists():
            return {"error": "File not found"}

        text = path.read_text()

        return {
            "file": str(path),
            "lines": len(text.splitlines()),
            "characters": len(text),
            "functions": text.count("def "),
            "classes": text.count("class "),
            "imports": text.count("import "),
            "todos": text.upper().count("TODO"),
            "content": text,
        }

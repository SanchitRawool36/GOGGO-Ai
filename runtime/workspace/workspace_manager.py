from pathlib import Path
import shutil


class WorkspaceManager:
    """
    Handles everything related to project workspaces.

    Create folders
    Create files
    Read files
    Update files
    Delete files
    Move files
    Copy files
    Project tree
    """

    def __init__(self, root="."):
        self.root = Path(root)

    # -------------------------
    # Helpers
    # -------------------------

    def _path(self, relative):
        return self.root / relative

    # -------------------------
    # Folder Operations
    # -------------------------

    def create_folder(self, folder):

        path = self._path(folder)

        path.mkdir(parents=True, exist_ok=True)

        return path

    # -------------------------
    # File Operations
    # -------------------------

    def create_file(self, filename, content=""):

        path = self._path(filename)

        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(content)

        return path

    def read_file(self, filename):

        return self._path(filename).read_text()

    def overwrite(self, filename, content):

        self._path(filename).write_text(content)

    def append(self, filename, content):

        with open(self._path(filename), "a") as f:
            f.write(content)

    def delete(self, filename):

        self._path(filename).unlink(missing_ok=True)

    # -------------------------
    # Move / Copy
    # -------------------------

    def move(self, src, dst):

        shutil.move(str(self._path(src)), str(self._path(dst)))

    def copy(self, src, dst):

        shutil.copy(str(self._path(src)), str(self._path(dst)))

    # -------------------------
    # Search
    # -------------------------

    def search(self, keyword):

        results = []

        for file in self.root.rglob("*"):

            if keyword.lower() in file.name.lower():

                results.append(str(file))

        return results

    # -------------------------
    # Project Tree
    # -------------------------

    def tree(self):

        files = []

        for p in self.root.rglob("*"):

            files.append(str(p.relative_to(self.root)))

        return sorted(files)
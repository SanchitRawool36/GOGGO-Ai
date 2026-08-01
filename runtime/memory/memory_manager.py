from __future__ import annotations


class MemoryManager:
    """Simple in-memory persistence for runtime state."""

    def __init__(self):
        self.entries = []

    def save(self, entry=None) -> None:
        if entry is None:
            entry = {"status": "saved"}
        self.entries.append(entry)

    def list(self):
        return list(self.entries)

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional
from uuid import uuid4


class AgentMemory:
    """Simple JSON-backed memory for an AI agent."""

    def __init__(self, agent_name: str, storage_path: Optional[str] = None) -> None:
        self.agent_name = agent_name
        self.storage_path = Path(storage_path or f"runtime/logs/{agent_name}_memory.json")
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        self.entries: List[Dict[str, Any]] = []
        self._load()

    def remember(self, key: str, value: Any) -> Dict[str, Any]:
        entry = {"id": str(uuid4()), "key": key, "value": value}
        self.entries.append(entry)
        self._save()
        return entry

    def forget(self, key: str) -> None:
        self.entries = [entry for entry in self.entries if entry.get("key") != key]
        self._save()

    def latest(self, limit: int = 5) -> List[Dict[str, Any]]:
        return list(reversed(self.entries[-limit:]))

    def search(self, keyword: str) -> List[Dict[str, Any]]:
        keyword = keyword.lower()
        return [entry for entry in self.entries if keyword in str(entry.get("value", "")).lower() or keyword in str(entry.get("key", "")).lower()]

    def summarize(self) -> Dict[str, Any]:
        return {"agent": self.agent_name, "entry_count": len(self.entries), "keys": sorted({entry["key"] for entry in self.entries})}

    def _load(self) -> None:
        if self.storage_path.exists():
            try:
                data = json.loads(self.storage_path.read_text(encoding="utf-8"))
                self.entries = data.get("entries", [])
            except json.JSONDecodeError:
                self.entries = []

    def _save(self) -> None:
        self.storage_path.write_text(json.dumps({"agent": self.agent_name, "entries": self.entries}, indent=2), encoding="utf-8")

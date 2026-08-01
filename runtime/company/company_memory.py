from datetime import datetime


class CompanyMemory:

    def __init__(self):

        self.memory = []

    # ----------------------
    # Add Knowledge
    # ----------------------

    def add(self, source, category, content):

        self.memory.append({

            "time": datetime.now(),

            "source": source,

            "category": category,

            "content": content

        })

    # ----------------------
    # Get Everything
    # ----------------------

    def all(self):

        return self.memory

    # ----------------------
    # Search
    # ----------------------

    def search(self, keyword):

        keyword = keyword.lower()

        return [

            item

            for item in self.memory

            if keyword in item["content"].lower()

            or keyword in item["category"].lower()

        ]

    # ----------------------
    # Latest
    # ----------------------

    def latest(self, limit=10):

        return self.memory[-limit:]

    # ----------------------
    # Clear
    # ----------------------

    def clear(self):

        self.memory.clear()
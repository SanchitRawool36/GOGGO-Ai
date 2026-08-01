from runtime.tasks.task import Task


class Inbox:

    def __init__(self):
        self.queue = []

    def add(self, task: Task):
        self.queue.append(task)

    def next(self):
        if not self.queue:
            return None
        return self.queue.pop(0)

    def pending(self):
        return len(self.queue)
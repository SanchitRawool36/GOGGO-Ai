from collections import defaultdict


class MessageBus:
    """
    Shared communication system between AI agents.
    """

    def __init__(self):

        self.messages = defaultdict(list)

    # -------------------------
    # Send
    # -------------------------

    def send(self, sender, receiver, message):

        self.messages[receiver].append({

            "from": sender,

            "message": message

        })

    # -------------------------
    # Receive
    # -------------------------

    def receive(self, receiver):

        inbox = self.messages.get(receiver, [])

        self.messages[receiver] = []

        return inbox

    # -------------------------
    # Peek
    # -------------------------

    def peek(self, receiver):

        return self.messages.get(receiver, [])

    # -------------------------
    # Clear
    # -------------------------

    def clear(self):

        self.messages.clear()
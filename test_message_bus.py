from runtime.messaging.message_bus import MessageBus

bus = MessageBus()

bus.send(

    "CEO",

    "CTO",

    "Please design authentication system."

)

bus.send(

    "CEO",

    "HR",

    "Prepare hiring roadmap."

)

bus.send(

    "CTO",

    "HR",

    "Need one backend developer."

)

print("=" * 60)

print("CTO INBOX")

print("=" * 60)

for msg in bus.receive("CTO"):

    print(msg)

print()

print("=" * 60)

print("HR INBOX")

print("=" * 60)

for msg in bus.receive("HR"):

    print(msg)
from runtime.router.model_router import ModelRouter
from runtime.self_healing.self_healer import SelfHealer

router = ModelRouter()

healer = SelfHealer(router)

healer.run("broken_program.py")
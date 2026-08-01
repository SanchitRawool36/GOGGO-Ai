from uuid import uuid4
from datetime import datetime

from pydantic import BaseModel


class Task(BaseModel):

    id: str = str(uuid4())

    title: str

    description: str

    assigned_to: str

    priority: str = "MEDIUM"

    status: str = "PENDING"

    created_at: datetime = datetime.now()
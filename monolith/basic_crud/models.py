from typing import Annotated
from pydantic import (
    StringConstraints,
    PositiveInt,
    BaseModel,
)

class Task(BaseModel):
    title: Annotated[str, StringConstraints(
        strip_whitespace=True,
        max_length=64,
        min_length=3,
        strict=True,
    )]
    content: Annotated[str, StringConstraints(
        strip_whitespace=False,
        max_length=2**16,
        strict=True,
    )]

class UpdateTask(Task):
    id: Annotated[int, PositiveInt]

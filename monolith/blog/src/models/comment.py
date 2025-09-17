from typing import Annotated
from pydantic import (
    StringConstraints,
    BaseModel,
)


# ~>
from src.models.enums import State


# <·
class Comment(BaseModel):
    post: Annotated[str, StringConstraints(
        strip_whitespace=True,
        max_length=128,
        min_length=128,
        strict=True,
    )]
    author: Annotated[str, StringConstraints(
        strip_whitespace=True,
        max_length=128, # uuid user len
    )]
    content: Annotated[str, StringConstraints(
        strip_whitespace=True,
        max_length=256,
        min_length=3,
    )]
    status: State

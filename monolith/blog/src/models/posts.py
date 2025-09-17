from typing import Annotated
from pydantic import (
    StringConstraints,
    BaseModel,
)


# ~>
from src.models.enums import State


# <·
class Post(BaseModel):
    title: Annotated[str,  StringConstraints(
        strip_whitespace=True,
        max_length=128,
        min_length=3,
        strict=True,
    )]
    content: Annotated[str, StringConstraints(
        max_length=256,
        min_length=3,
    )]
    author: Annotated[str, StringConstraints(
        strip_whitespace=True,
        max_length=128,
        min_length=128,
        strict=True,
    )]
    categories: list
    tags: list
    images: list # validate before
    status: State

from typing import Annotated
from pydantic import (
    StringConstraints,
    BaseModel,
    EmailStr,
)


# <·
class User(BaseModel):
    name: Annotated[str,  StringConstraints(
        strip_whitespace=True,
        max_length=64,
        min_length=3,
        strict=True,
    )]
    email: Annotated[str, EmailStr]
    password: Annotated[str, StringConstraints(
        strip_whitespace=True,
        max_length=128,
        min_length=3,
        strict=True,
    )]
    # custom future
    # avatar_img: Annotated[bytes, validate_image]

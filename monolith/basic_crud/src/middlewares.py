from fastapi import Request


#~>
from .result import (
    Result,
    Ok,
)


#<·
def log_mw(req: Request) -> Result[None, str]:
    print(req.headers)

    return Ok()

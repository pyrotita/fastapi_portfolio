from fastapi import Request, HTTPException


#~>
from .jwt import JwtHandler


#<·
class Middleware:
    def __init__(self, level_permise: int) -> None:
        self._level_permise: int = level_permise
        self.__jwt_handler: JwtHandler = JwtHandler()

    async def __call_(self, req: Request):
        auth_header = req.headers.get('Authorization')

        if not auth_header:
            raise HTTPException(
                detail='Missing or invalid Authorization header',
                status_code=401,
            )

        token: str = auth_header.split()[1]

        try:
            payload = self.__jwt_handler.read_jwt(token=token)


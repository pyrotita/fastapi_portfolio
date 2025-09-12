from fastapi import APIRouter, HTTPException
from typing import Any


#<·
class EndPoint:
    def __init__(
        self,
        app: APIRouter,

        method: str = 'get',
        route: str = '/',
    ) -> None:
        self._app: APIRouter = app
        self._method: str = method
        self._route: str = route

        self._middlewares: list = []


    def use_mw(self, middlewares: list):
        self._middlewares.extend(middlewares)

        return self


    def __exec_middlewares(self) -> None:
        for middleware in self._middlewares:
            if ( err_mw := middleware() ).is_err():
                raise HTTPException(
                    detail=err_mw.error,
                    status_code=401,
                )


    def build(self) -> None:
        self.__exec_middlewares()

        self._app.add_api_route(
            path=self._route,
            methods=[self._method.upper()],
            endpoint=self.endpoint,
        )


    def endpoint(self) -> Any: ...

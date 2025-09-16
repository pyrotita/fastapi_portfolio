from fastapi import APIRouter


# ¿?
from database import LogDB


# ~>
from utils.endpoint import EndPoint


# <·
class CreateLog(EndPoint):
    def __init__(self, app: APIRouter, database: LogDB) -> None:
        super().__init__(
            method='post',
            app=app,
        )


    def endpoint(self, log: Log) -> None: # type: ignore
        ...

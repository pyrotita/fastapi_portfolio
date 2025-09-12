from typing import Optional
from fastapi import APIRouter, HTTPException


#¿?
from database import TasksDB


#~>
from src.endpoint import EndPoint


#<·
class ReadTask(EndPoint):
    def __init__(self, app: APIRouter, database: TasksDB) -> None:
        self.__task_db: TasksDB = database

        super().__init__(
            method='{iden}',
            app=app,
        )


    def endpoint(self, iden: int) -> Optional[tuple]:
        try:
            return self.__task_db.read_one(iden)

        except Exception as e:
            print(e)

            raise HTTPException(
                detail='Internal error',
                status_code=500,
            )



from fastapi import APIRouter, HTTPException
from pydantic import PositiveInt
from typing import Optional


#¿?
from database import TasksDB


#~>
from src.endpoint import EndPoint


#<·
class DeleteTask(EndPoint):
    def __init__(self, app: APIRouter, database: TasksDB) -> None:
        self.__task_db: TasksDB = database

        super().__init__(
            method='delete',
            app=app,
        )


    def endpoint(self, id: PositiveInt) -> Optional[int]: # type: ignore
        try:
            return self.__task_db.delete(id=id)

        except Exception as e:
            print(e)

            raise HTTPException(
                detail='Internal error',
                status_code=500,
            )

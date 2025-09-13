from fastapi import APIRouter, HTTPException
from typing import Optional


#¿?
from database import TasksDB


#~>
from src.endpoint import EndPoint
from models import UpdateTask



#<·
class ModifyTask(EndPoint):
    def __init__(self, app: APIRouter, database: TasksDB) -> None:
        self.__task_db: TasksDB = database

        super().__init__(
            method='put',
            app=app,
        )


    def endpoint(self, task: UpdateTask) -> Optional[tuple]: # type: ignore
        try:
            task: tuple[int, str, str] = (task.id, task.title, task.content)
            return self.__task_db.update(
                t=task,
            )

        except Exception as e:
            print(e)

            raise HTTPException(
                detail='Internal error',
                status_code=500,
            )


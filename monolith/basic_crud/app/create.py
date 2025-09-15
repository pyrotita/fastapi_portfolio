from fastapi import APIRouter, HTTPException


#¿?
from database import TasksDB


#~>
from src.endpoint import EndPoint
from models import Task



#<·
class CreateTask(EndPoint):
    def __init__(self, app: APIRouter, database: TasksDB) -> None:
        self.__task_db: TasksDB = database

        super().__init__(
            method='post',
            app=app,
        )


    def endpoint(self, task: Task) -> int: # type: ignore
        try:
            return self.__task_db.create(
                title=task.title,
                content=task.content,
            )[0]

        except Exception as e:
            print(e)

            raise HTTPException(
                detail='Internal error',
                status_code=500,
            )

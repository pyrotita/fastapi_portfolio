from fastapi import APIRouter


#¿?
from database import TasksDB

#~>
from .create import CreateTask
from .read import ReadTask

from src.middlewares import log_mw


#<·
router: APIRouter = APIRouter(
    prefix='/tasks',
)

DATABASE: TasksDB = TasksDB()


CreateTask(
    database=DATABASE,
    app=router,
).use_mw(middlewares=[log_mw,]).build()

ReadTask(
    database=DATABASE,
    app=router,
).use_mw(middlewares=[log_mw,]).build()

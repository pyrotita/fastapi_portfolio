from fastapi import APIRouter


#¿?
from database import TasksDB

#~>
from .read_all import ReadAllTask
from .update import ModifyTask
from .delete import DeleteTask
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
).use_mw(middlewares=[log_mw]).build()


ReadAllTask(
    database=DATABASE,
    app=router,
).use_mw(middlewares=[log_mw]).build()


DeleteTask(
    database=DATABASE,
    app=router,
).use_mw(middlewares=[log_mw]).build()


ModifyTask(
    database=DATABASE,
    app=router,
).use_mw(middlewares=[log_mw]).build()


ReadTask(
    database=DATABASE,
    app=router,
).use_mw(middlewares=[log_mw]).build()




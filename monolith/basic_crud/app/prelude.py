from fastapi import APIRouter


#¿?
from database import TasksDB

#~>
from .read_all import ReadAllTask
from .update import ModifyTask
from .create import CreateTask
from .delete import DeleteTask
from .read import ReadTask

from src.middlewares import log_mw


#<·
router: APIRouter = APIRouter(
    prefix='/tasks',
)

DATABASE: TasksDB = TasksDB()

endpoints: tuple = (
    CreateTask,
    ReadAllTask,
    DeleteTask,
    ModifyTask,
    ReadTask,
)

for endpoint_cls in endpoints:
    endpoint_cls(
        database=DATABASE,
        app=router,
    ).use_mw(middlewares=[log_mw]).build()



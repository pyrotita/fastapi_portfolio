from fastapi import APIRouter


# ¿?
from database import LogDB


# ~>
from .create import CreateLog
from .read import ReadLog
from .read_all import ReadAllLogs


# <·
router: APIRouter = APIRouter()

DATABASE: LogDB = LogDB()


CreateLog(
    database=DATABASE,
    app=router,
).use_mw(middlewares=[]).build()

from typing import Optional
from fastapi import FastAPI, HTTPException

#¿?
from database import TasksDB

#~>
from models import (
    UpdateTask,
    Task,
)

#<·
app: FastAPI = FastAPI(
    title='monolith v0.1',
    debug=False,
)

DATABASE: TasksDB = TasksDB()


@app.post('/')
def create(t: Task) -> int:
    try:
        return DATABASE.create(
            title=t.title,
            content=t.content,
        )[0]

    except Exception as e:
        print(e)

        raise HTTPException(
            detail='Internal error',
            status_code=500,
        )


@app.get('/all')
def get_all() -> list[tuple]:
    try:
        return DATABASE.read_all()

    except Exception as e:
        print(e)

        raise HTTPException(
            detail='Internal error',
            status_code=500,
        )


@app.get('/{iden}')
def get_one(iden: int) -> Optional[tuple]:
    try:
        return DATABASE.read_one(iden)

    except Exception as e:
        print(e)

        raise HTTPException(
            detail='Internal error',
            status_code=500,
        )


@app.put('/')
def update_task(t: UpdateTask) -> Optional[tuple]:
    try:
        task: tuple[int, str, str] = (t.id, t.title, t.content)
        return DATABASE.update(
            t=task,
        )

    except Exception as e:
        print(e)

        raise HTTPException(
            detail='Internal error',
            status_code=500,
        )


@app.delete('/')
def delete(id: int):
    try:
        return DATABASE.delete(id=id)

    except Exception as e:
        print(e)

        raise HTTPException(
            detail='Internal error',
            status_code=500,
        )



from fastapi import FastAPI


#~>
from app.prelude import router as task_router


#<·
app: FastAPI = FastAPI(
    title='monolith v0.1',
    debug=False,
)

app.include_router(task_router)


if __name__ == '__main__':
    from uvicorn import run

    run(
        host='127.0.0.1',
        port=3000,
        app=app,
    )


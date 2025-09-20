from fastapi import FastAPI


from app.prelude import router


app: FastAPI = FastAPI(
    title='Users',
    debug=False,
)

app.include_router(router)



if __name__ == '__main__':
    from uvicorn import run

    run(
        port=3000,
        app=app,
    )

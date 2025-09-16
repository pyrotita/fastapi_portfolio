from fastapi import FastAPI


# <·
app: FastAPI = FastAPI()



if __name__ == '__main__':
    from uvicorn import run


    run(
        port=3100,
        app=app,
    )

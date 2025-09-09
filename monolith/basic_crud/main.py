from fastapi import FastAPI


app: FastAPI = FastAPI(
    title='Basic crud impl',
    debug=False,
)

@app.get('/')
def root() -> dict:
    return {}

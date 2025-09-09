from fastapi import FastAPI

#¿?
from database import Tasks


#<·
app: FastAPI = FastAPI(
    title='Basic crud impl',
    debug=False,
)

@app.get('/')
def root(iden: str) -> dict:
    return {}

from app import app


if __name__ == '__main__':
    from uvicorn import run

    run(
        host='127.0.0.1',
        port=3000,
        app=app,
    )

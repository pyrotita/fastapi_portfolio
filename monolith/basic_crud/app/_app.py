f
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



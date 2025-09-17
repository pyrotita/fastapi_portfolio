from fastapi import FastAPI


#~>
from app.comment.prelude import router as comment_router
from app.admin.prelude import router as admin_router
from app.posts.prelude import router as posts_router
from app.user.prelude import router as user_router
from app.auth.prelude import router as auth_router


#<·
app: FastAPI = FastAPI(
    title='monolith v0.1',
    debug=False,
)

# ruters
app.include_router(comment_router)
app.include_router(admin_router)
app.include_router(posts_router)
app.include_router(user_router)
app.include_router(auth_router)


if __name__ == '__main__':
    from uvicorn import run

    run(
        host='127.0.0.1',
        port=3000,
        app=app,
    )


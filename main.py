from datetime import datetime
from enum import Enum
from typing import List, Optional, Union
from typing_extensions import Annotated
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import pkg_resources
from fastapi.templating import Jinja2Templates

# from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from fastapi_users import fastapi_users, FastAPIUsers
from pydantic import BaseModel, Field

from fastapi import FastAPI, Request, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse

# from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager

# from auth.schemas import UserRead, UserCreate

from auth.auth import auth_backend
from auth.schemas import UserRead, UserCreate, UserUpdate

import uvicorn

app = FastAPI(title="Trading App")

origins = [
    "https://localhost:8001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=[
        "date",
        "Access-Control-Allow-Origin",
        "vary",
        "Set-Cookie",
        "Server",
    ],
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

# Роутер для авторизации (/auth/jwt/login и /auth/jwt/logout)
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

# Роутер для регистрации (/auth/register)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

# Роутер для верификации (/auth/verify и /auth/request-verify-token)
# app.include_router(
#     fastapi_users.get_verify_router(UserRead),
#     prefix="/auth",
#     tags=["auth"],
# )

# Роутер для сброса и восстановления пароля (/auth/forgot-password и /auth/reset-password)
# app.include_router(
#     fastapi_users.get_reset_password_router(),
#     prefix="/auth",
#     tags=["auth"],
# )


current_user = fastapi_users.current_user()


@app.get("/current_user")
def protected_route(user: User = Depends(current_user)):
    return f"Hello current_user, username: {user.username}, ' email: ', {user.email}, registered_at: {user.registered_at}, first_name: {user.first_name}"

current_active_user = fastapi_users.current_user(active=True)

@app.get("/current_active_user")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello active current_user, {user.username}, ' email: ', {user.email}"

app.mount(
    "/static",
    StaticFiles(
        directory="C:\\Users\\mag\\Documents\\fastAPI_app\\fastAPI_client\\build\\static"
    ),
    name="static",
)

templates = Jinja2Templates(
    directory="C:\\Users\\mag\\Documents\\fastAPI_app\\fastAPI_client\\build"
)


@app.get("/{full_path:path}")
def unprotected_route(request: Request, full_path: str):
    # return f"Hello, anonym"
    # return HTMLResponse(pkg_resources.resource_string(__name__, "index.html"))
    return templates.TemplateResponse("index.html", {"request": request})


# Запуск командой python main.py
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8001,
        log_level="info",
        reload=True,
        ssl_keyfile="./ssl/key.pem",
        ssl_certfile="./ssl/sert.pem",
    )

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

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

import uvicorn
import time
from datetime import date
import asyncio
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import os
from pathlib import Path

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


async def my_func_2():
    print("Func2 started..!!")
    await asyncio.sleep(6)
    print("Func2 ended..!!")

    return "b..!!"


@app.get("/imitation")
async def imitation():
    start = time.time()
    futures = [my_func_2()]
    b = await asyncio.gather(*futures)
    end = time.time()
    print("It took {} seconds to finish execution.".format(round(end - start)))
    return "Hello!"


@app.get("/checksums")
async def ckecksums():
    res = {
        "  *include\\ASF\\asf.h": "58cd3549e8a3f66410566c7f8c2738bd",
        " + *include\\ASF\\common\\services\\sleepmgr\\sleepmgr.h": "6a80cf5cdd180fbb5c712fbd3a0c7485",
        " + *include\\ASF\\common\\services\\sleepmgr\\samd\\conf_sleepmgr.h": "1f2376a8979ba50f4bdd16e966d39e86",
        " + *include\\ASF\\common\\services\\sleepmgr\\samd\\sleepmgr.h": "67024e2cb5ebb901ca7f9c117f1894d3",
        " + *include\\ASF\\common\\utils\\interrupt.h": "85f14bffc877ab0a071bae0f77cdce0f",
        " + *include\\ASF\\common\\utils\\parts.h": "61e25548b4ffff778601468e1b5073fd",
        " + *include\\ASF\\common\\utils\\interrupt\\interrupt_sam_nvic.h": "52fafee543eb6d9fed17075b266764c5",
        "  *include\\ASF\\sam0\\drivers\\ac\\_ac.h": "d9706a964da14b03e03e372ce096273c",
        "  *include\\ASF\\sam0\\drivers\\adc\\adc_feature.h": "6a5cfc19c74d799be204da11f6678c47",
        "  *include\\ASF\\sam0\\drivers\\adc\\_adc.h": "69f05f2 a6b178076c41c270efc4eea88",
        "  *include\\ASF\\sam0\\drivers\\dac\\dac_feature.h": "8023c3febe6efcf446d880600145576e",
        "  *include\\ASF\\sam0\\drivers\\dac\\_dac.h": "36fd69681e07c51290987fc709a6a3ac",
        "  *include\\ASF\\sam0\\drivers\\extint\\extint.h": "5c9719eb6651c1458b556c02511fa8e2",
        "  *include\\ASF\\sam0\\drivers\\extint\\extint_callback.h": "8a56239cd7f2b9ab6a281deba95c591a",
        "  *include\\ASF\\sam0\\drivers\\extint\\module_config\\conf_extint.h": "5777f4c07e5ece07153d17b3b7bb8ca3",
        "  *include\\ASF\\sam0\\drivers\\nvm\\nvm.h": "fc545e3fbe08ca6268abe5cacd269856",
        "  *include\\ASF\\sam0\\drivers\\port\\port.h": "0f97fe3d0d009965fc920da8114f1563",
        "  *include\\ASF\\sam0\\drivers\\port\\quick_start\\qs_port_basic.h": "46e2430194ab38b2b94821f497a9281e",
        "  *include\\ASF\\sam0\\drivers\\rtc\\rtc_calendar.h": "527dc6c3ff018b294b130d9f77fc179b",
        "  *include\\ASF\\sam0\\drivers\\sercom\\sercom_interrupt.h": "397bf09c8f15a766aac953d3055a5b72",
        "  *include\\ASF\\sam0\\drivers\\sercom\\sercom_pinout.h": "d9e96f774909c0f15cf8a51aa17aeed6",
        "  *include\\ASF\\sam0\\drivers\\sercom\\_sercom.h": "f5c35017ebc5a027d8a32c5b8e083e06",
        " - *include\\ASF\\sam0\\drivers\\sercom\\spi\\conf_spi.h": "150791721c2b6de2055513f7ef0d1576",
        " + *include\\ASF\\sam0\\drivers\\sercom\\spi\\conf_spi.h": "0dd23a55b861080f4a8302c3350146d9",
        "  *include\\ASF\\sam0\\drivers\\sercom\\spi\\_spi.h": "0d85c8c0fd5b5e0c0a1785802ee874b0",
        "  *include\\ASF\\sam0\\drivers\\sercom\\usart\\usart.h": "d4a5930515cba8ab183989992603ec30",
        "  *include\\ASF\\sam0\\drivers\\sercom\\usart\\usart_interrupt.h": "3baa948b38381dd375264ce80247050d",
        "  *include\\ASF\\sam0\\drivers\\system\\system.h": "b74e93148feae13f35da35b18b8e1592",
        "  *include\\ASF\\sam0\\drivers\\system\\clock\\reset.h": "d363540aaab95f47b01c839019f41c21",
        "  *include\\ASF\\sam0\\drivers\\system\\clock\\_clock.h": "75a695637851f4c57ef71ea5a9ef714e",
        "  *include\\ASF\\sam0\\drivers\\system\\clock\\_gclk.h": "4f7f07bc87fe38b2707eaae04379c132",
        "  *include\\ASF\\sam0\\drivers\\system\\clock\\clock_samd20\\clock_config_check.h": "bf7459cfa3feaf1bb2481bc5b0e8d695",
        "  *include\\ASF\\sam0\\drivers\\system\\clock\\clock_samd20\\clock_feature.h": "289536d5f566c199a97c719e1592645f",
        "  *include\\ASF\\sam0\\drivers\\system\\clock\\clock_samd20\\conf_clocks.h": "1463d6266d70107ab91220adc1e64d5c",
        "  *include\\ASF\\sam0\\drivers\\system\\interrupt\\system_interrupt.h": "37fdf7f888c4a8c67f4fc609a60fb550",
        "  *include\\ASF\\sam0\\drivers\\system\\interrupt\\system_interrupt_samd20\\system_interrupt_features.h": "62226eedb5886f14bc12811acec669f1",
        "  *include\\ASF\\sam0\\drivers\\system\\pinmux\\pinmux.h": "84dafeeb31d98fdfcc2408e51c7ebc85",
        "  *include\\ASF\\sam0\\drivers\\system\\power\\power_sam_d_r_h\\power.h": "a931e0ad657117514a152a0540462780",
        "  *include\\ASF\\sam0\\drivers\\system\\reset\\reset_sam_d_r_h\\reset.h": "d363540aaab95f47b01c839019f41c21",
        "  *include\\ASF\\sam0\\drivers\\tc\\conf_qs_tc_timer.h": "01a0a15e788bb369e1ba4bf86f53b28f",
        "  *include\\ASF\\sam0\\drivers\\tc\\tc_interrupt.h": "4d8f1e7a2b78a33e1c2141523f46197b",
        "  *include\\ASF\\sam0\\drivers\\tc\\_tc.h": "f00f28e2d105813047133195c6b2605b",
        "  *include\\ASF\\sam0\\drivers\\wdt\\_wdt.h": "84b7d20c4e4167dac79abbb53d83fc05",
        "  *include\\ASF\\sam0\\utils\\compiler.h": "98be6882a2479b7a009d1d7142514500",
    }
    return res


@app.get("/compare_unused_functions")
async def compare_unused_functions():
    res = {
        "new_files": {
            "\\source\\test.c": ["checker                                 12"],
            "\\source\\system\\system_functions.c": [
                "__attribute__                          389",
                "__attribute__                          403",
            ],
        },
        "deleted_files": {
            "\\source\\device\\startup_samd20.c": [
                "Dummy_Handler                          235"
            ],
            "\\source\\system\\volume_control.c": [
                "__attribute__                           68"
            ],
            "\\source\\gui\\flash_fs.cpp": [
                "CFlashFile::CFlashFile                 596",
                "CFlashStreamFile::CFlashStreamFile     877",
            ],
        },
        "same_files": {
            "\\include\\ASF\\thirdparty\\CMSIS\\Include\\cmsis_gcc.h": [
                "packed                                  74",
                "T_UINT16_READ                           90",
                "T_UINT16_WRITE                          82",
            ]
        },
        "modified_functions": {
            " + \\source\\asf\\system.c": [
                "_system_dummy_init                      45",
                "Комсомольск                             24",
            ],
            " - \\source\\system\\battery.c": [
                "__attribute__                           26",
                "T_UINT16_READ                           93",
            ],
            " + \\source\\system\\battery.c": [
                "spi_transceive_buffer_wait            1014",
                "что-то ещё                         1231124",
            ],
        },
    }
    return res


@app.get("/analyze_sources")
async def analyse_sources():
    res = {
        "python": 172,
        "javascript": 41,
        "java": 0,
        ".h files": 188,
        "c": 51,
        "c++": 116,
        "c#": 0,
        "php": 0,
        "swift": 0,
        "typescript": 0,
        "ruby": 0,
        "go": 0,
        "rust": 0,
        "kotlin": 0,
        "perl": 0,
        "scala": 0,
        "objective-c": 0,
        "shell": 0,
        "sql": 0,
        "html": 17,
        "css": 4,
        "assembler": 2,
        "binary_files": {
            "windows_files": [
                "\\2.1\\Web\\htps\\Denwer3_Base_2013-06-02_a2.2.22_p5.3.13_m5.5.25_pma3.5.1_xdebug.exe",
                "\\2.1\\Ооп\\Alexseev_PW_8_7.exe",
                "\\2.1\\Ооп\\Alexseev_PW_8_8.exe",
                "\\2.1\\Ооп\\Alexseev_PW_8_9.exe",
                "\\2.1\\Ооп\\Alexseev_PZ_7.exe",
                "\\2.1\\Ооп\\Alexseev_PZ_8_10-.exe",
                "\\2.1\\Ооп\\ClassStruct\\Debug\\ClassStruct.exe",
                "\\2.1\\Ооп\\ConsoleApplication1\\Debug\\ConsoleApplication1.exe",
                "\\2.1\\Ооп\\FinalStruct\\Debug\\FinalStruct.exe",
                "\\2.1\\Ооп\\Project4\\Debug\\Project4.exe",
                "\\2.1\\Ооп\\Project5\\Debug\\Project5.exe",
                "\\2.1\\Ооп\\Project5\\Release\\Project5.exe",
                "\\2.1\\Ооп\\PW8R\\Debug\\PW8R.exe",
                "\\2.1\\Ооп\\PW8R\\Release\\PW8R.exe",
            ],
            "linux_files": [],
            "empty_files": [
                "\\2.1\\Английский\\фвыавп.txt",
                "\\2.1\\Ооп\\Алексеев\\file5out.txt",
                "\\2.1\\Программирование\\Python\\PlayGround.py",
                "\\2.1\\Программирование\\Stepik\\testzone.py",
                "\\2.1\\Социология\\Ответы на вопросы.docx",
                "\\2.1\\Философия\\Проект Интернет\\Выступление.pptx",
                "\\include\\ASF\\thirdparty\\CMSIS\\Training_The_Demon-0.1.0-win\\lib\\python3.9\\future\\backports\\test\\nullcert.pem.pyc",
                "\\include\\ASF\\thirdparty\\P4G Mods\\.Reloaded II\\portable.txt",
                "\\include\\ASF\\thirdparty\\P4G Mods\\.Reloaded II\\Mods\\p4gpc.communityenhancementpack12\\FEmulator\\PAK\\facility\\book.arc\\book.bf",
                "\\include\\ASF\\thirdparty\\P4G Mods\\.Reloaded II\\Mods\\p4gpc.communityenhancementpack12\\FEmulator\\PAK\\field\\pack\\fd006_001.arc\\n006_001.bf",
                "\\include\\ASF\\thirdparty\\P4G Mods\\.Reloaded II\\Mods\\p4gpc.communityenhancementpack12\\FEmulator\\PAK\\field\\pack\\fd006_003.arc\\n006_003.bf",
                "\\include\\ASF\\thirdparty\\P4G Mods\\.Reloaded II\\Mods\\p4gpc.communityenhancementpack12\\FEmulator\\PAK\\field\\pack\\fd007_001.arc\\n007_001.bf",
                "\\include\\ASF\\thirdparty\\P4G Mods\\.Reloaded II\\Mods\\p4gpc.communityenhancementpack12\\FEmulator\\PAK\\field\\pack\\fd009_004.arc\\n009_004.bf",
            ],
        },
    }
    return res


tmp_file_dir = "/tmp/example-files"
Path(tmp_file_dir).mkdir(parents=True, exist_ok=True)


@app.post("/file/upload_understand_new_file")
async def upload_file(file: UploadFile):
    # file.file.read().decode("utf8")
    with open(os.path.join(tmp_file_dir, file.filename), "wb") as disk_file:
        file_bytes = await file.read()
        disk_file.write(file_bytes)
        print(
            f"Received file named {file.filename} containing {len(file_bytes)} bytes. "
        )
        return FileResponse(
            disk_file.name, filename=file.filename, media_type=file.content_type
        )


@app.post("/file/upload_understand_old_file")
async def upload_file(file: UploadFile):
    # file.file.read().decode("utf8")
    with open(os.path.join(tmp_file_dir, file.filename), "wb") as disk_file:
        file_bytes = await file.read()
        disk_file.write(file_bytes)
        print(
            f"Received file named {file.filename} containing {len(file_bytes)} bytes. "
        )
        return FileResponse(
            disk_file.name, filename=file.filename, media_type=file.content_type
        )


root_client_dir = "C:\\Users\\user\\fastAPI_client\\build"

app.mount(
    "/static",
    StaticFiles(directory=root_client_dir + "\\static"),
    name="static",
)

templates = Jinja2Templates(directory=root_client_dir)


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

# from fastapi import FastAPI, APIRouter, Depends
# from fastapi.middleware.cors import CORSMiddleware
# import models.models as models
# from config import engine

# # from routes import router
# from static_analysis.routes_static_analysis import router_static_analysis
# from accounts.routes_accounts import router_accounts
# from projects.routes_projects import router_projects

# # from routes_static_analysis import router_static_analysis
# import uvicorn

# # for OAuth authorization
# from fastapi.security import OAuth2PasswordBearer
# from typing_extensions import Annotated

# # router = APIRouter(
# #     prefix="/products",
# #     tags=["Product"]
# # )


# # Создает модели(таблицы) в БД
# models.Base.metadata.create_all(bind=engine)

# # Создание экземпляра класса FastAPI
# app = FastAPI()

# # Фунция, которая работает с каждым запросом перед обработкой этого запроса соответствующей функцией (напр. @app.get('/'))
# app.add_middleware(
#     CORSMiddleware,
#     # Cross-Origin Resource Sharing (CORS) - разрешаем все внешние подключения
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# @app.get("/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}


# # @app.get("/items/")
# # async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
# #     return {"token": token}


# # async def root():
# #     return {"message": "Hello World"}

# # if __name__ == "__main__":
# #     uvicorn.run("server:app", host="localhost", port=8000, reload=True)


# # @router.get("/")
# # async def get_by_id2():
# #     # _book = crud.get_book_by_id(db, id)
# #     # return Response(code=200, status="Ok", message="Success get data", result=_book).dict(exclude_none=True)
# #     return "Congratulations!"

# # app.include_router(router, prefix="/book", tags=["book"])

# # Подключаем остальные обработчики запросов (из routes.py)
# # app.include_router(router)
# app.include_router(router_static_analysis)
# app.include_router(router_accounts)
# app.include_router(router_projects)

# # Запуск командой python main.py
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info", reload=True)

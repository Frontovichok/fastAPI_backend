from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
import model
from config import engine
from routes import router
import uvicorn

# router = APIRouter(
#     prefix="/products",
#     tags=["Product"]
# )


# Создает модели(таблицы) в БД
model.Base.metadata.create_all(bind=engine)

# Cross-Origin Resource Sharing (CORS) - разрешаем все внешние подключения
origins = ["*"]

# Создание экземпляра класса FastAPI
app = FastAPI()

# Фунция, которая работает с каждым запросом перед обработкой этого запроса соответствующей функцией (напр. @app.get('/'))
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/board")
async def root():
    board_data = {
        'tasks': {
            'task-1': {'id': 'task-1', 'content': 'create video'},
            'task-2': {'id': 'task-2', 'content': 'edit video'},
            'task-3': {'id': 'task-3', 'content': 'publish video'}
        },
        'columns': {
            'column-1': {
                'id': 'column-1',
                'title': 'To do',
                'taskIds': ['task-2', 'task-3']
            },
            'column-2': {
                'id': 'column-2',
                'title': 'Done',
                'taskIds': ['task-1']
            }
        },
        'columnOrder': ['column-1', 'column-2']
    }
    return {"board": board_data}


@app.get('/')
async def Home():
    print("hello Home")
    return "Welcome Home"


# async def root():
#     return {"message": "Hello World"}

# if __name__ == "__main__":
#     uvicorn.run("server:app", host="localhost", port=8000, reload=True)


# @router.get("/")
# async def get_by_id2():
#     print("hello router 1")
#     # _book = crud.get_book_by_id(db, id)
#     # return Response(code=200, status="Ok", message="Success get data", result=_book).dict(exclude_none=True)
#     return "Congratulations!"

# app.include_router(router, prefix="/book", tags=["book"])

# Подключаем остальные обработчики запросов (из routes.py)
app.include_router(router)

# Запуск командой python main.py
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000,
                log_level="info", reload=True)
    print("running")

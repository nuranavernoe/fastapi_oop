# запуск сервера
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from api.router import router as api_router

app = FastAPI()

origins = [
    "http://localhost:5173",

]

app.include_router(api_router, prefix="/api")
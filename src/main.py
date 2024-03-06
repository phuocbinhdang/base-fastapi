from fastapi import FastAPI
from src.database import init_database
from src.user.router import router as user_router

init_database()
app = FastAPI()

app.include_router(user_router)

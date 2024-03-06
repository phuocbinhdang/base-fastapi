from fastapi import APIRouter
from src.user.dto import CreateDTO
from src.user.service import UserService

router = APIRouter(prefix="/api/user", tags=["user"])
user_service = UserService()


@router.post("/")
def create(request: CreateDTO):
    return user_service.create(request)

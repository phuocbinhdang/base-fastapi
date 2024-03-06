from src.user.repository import UserRepository
from src.user.dto import CreateDTO
from src.user.entity import User


class UserService:
    user_repository = UserRepository()

    def create(self, request: CreateDTO):
        user = User(name=request.name)
        return self.user_repository.create(user)

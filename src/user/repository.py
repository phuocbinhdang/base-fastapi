from src.repository import BaseRepository
from src.user.entity import User


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__()

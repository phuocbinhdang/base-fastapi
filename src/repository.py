from typing import TypeVar, Generic, List
from src.database import Base, get_session

T = TypeVar("T", bound=Base)


class BaseRepository(Generic[T]):
    def __init__(self):
        pass

    def create(self, data: T) -> T:
        with get_session() as session:
            session.add(data)
            session.commit()
            session.refresh(data)

            return data

    def update(self, id, data: T) -> T:
        with get_session() as session:
            session.query(T).filter_by(id=id).update(data)

            return data

    def delete(self, id) -> None:
        with get_session() as session:
            session.query(T).filter_by(id=id).delete()

            return None

    def find_by_id(self, id) -> T:
        with get_session() as session:
            return session.query(T).filter_by(id=id).first()

    def find_all(self, offset=None, limit=None) -> List[T]:
        with get_session() as session:
            return session.query(T).offset(offset).limit(limit).all()

    def count_all(self) -> int:
        with get_session() as session:
            return session.query(T).count()

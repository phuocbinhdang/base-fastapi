from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

from src import config

db_engine = create_engine(config.DB_URL)

session_factory = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=db_engine,
)
Session = scoped_session(session_factory)

Base = declarative_base()


@contextmanager
def get_session():
    session = Session()
    try:
        yield session
    except:
        session.rollback()
    finally:
        session.close()


def init_database():
    Base.metadata.create_all(db_engine)

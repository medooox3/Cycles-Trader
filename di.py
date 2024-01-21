"""Dependency Injection Module"""

from sqlmodel import Session
from database import engine
from fastapi import Depends
from typing import Annotated


def get_session():
    with Session(engine) as session:
        yield session


# Type alias
DBSession = Annotated[Session, Depends(get_session)]

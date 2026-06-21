from sqlalchemy import Column, Integer, String
from .database import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        index=True
    )

    email = Column(
        String,
        unique=True,
        index=True
    )

    hashed_password = Column(
        String
    )

    notes = relationship(
        "Note",
        back_populates="owner"
    )

class Note(Base):

    __tablename__ = "notes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(String)

    content = Column(String)

    owner_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    owner = relationship(
        "User",
        back_populates="notes"
    )
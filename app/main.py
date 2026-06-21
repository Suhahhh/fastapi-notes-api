

from fastapi import FastAPI, HTTPException
from fastapi import UploadFile, File
import shutil
from .database import engine
from .models import User, Note
from .database import Base
from sqlalchemy.orm import Session
from fastapi import Depends
from .auth import hash_password
from .database import get_db
from . import schemas
from .auth import (
    verify_password,
    create_access_token
)


Base.metadata.create_all(
    bind=engine
)

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Notes API Running"
    }
@app.post("/register", status_code=201)
def register_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(
            user.password
        )
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message":
        "User registered successfully"
    }

@app.post("/login")
def login(
    user: schemas.UserLogin,
    db: Session = Depends(get_db)
):

    db_user = (
        db.query(User)
        .filter(
            User.email == user.email
        )
        .first()
    )

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {
            "user_id": db_user.id
        }
    )

    return {
        "access_token": token
    }

@app.post("/notes", status_code=201)
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(get_db)
):

    new_note = Note(
        title=note.title,
        content=note.content,
        owner_id=1
    )

    db.add(new_note)

    db.commit()

    db.refresh(new_note)

    return new_note

@app.get("/notes")
def get_notes(
    db: Session = Depends(get_db)
):

    return db.query(Note).all()

@app.put("/notes/{note_id}")
def update_note(
    note_id: int,
    note: schemas.NoteCreate,
    db: Session = Depends(get_db)
):

    db_note = (
        db.query(Note)
        .filter(Note.id == note_id)
        .first()
    )

    if not db_note:

        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    db_note.title = note.title
    db_note.content = note.content

    db.commit()

    return db_note

@app.delete("/notes/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db)
):

    db_note = (
        db.query(Note)
        .filter(Note.id == note_id)
        .first()
    )

    if not db_note:

        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    db.delete(db_note)

    db.commit()

    return {
        "message":
        "Note deleted"
    }

@app.post("/upload")
def upload_file(
    file: UploadFile = File(...)
):

    file_path = (
        f"uploads/{file.filename}"
    )

    with open(
        file_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "message":
        "File uploaded successfully",
        "filename":
        file.filename
    }
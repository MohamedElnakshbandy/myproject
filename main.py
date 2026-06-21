from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import User

app = FastAPI()


class UserCreate(BaseModel):
    name: str
    email: str


class UserUpdate(BaseModel):
    name: str
    email: str


@app.get("/")
def home():
    return {"message": "FastAPI + PostgreSQL is working!"}


@app.get("/users")
def get_users(db: Session = Depends(get_db)):

    users = db.query(User).all()

    result = []

    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })

    return result


@app.get("/user-count")
def user_count(db: Session = Depends(get_db)):

    count = db.query(User).count()

    return {"total_users": count}


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return {"error": "User not found"}

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }


@app.post("/users")
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    try:

        new_user = User(
            name=user.name,
            email=user.email
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            "message": "User created successfully",
            "id": new_user.id
        }

    except Exception as e:

        db.rollback()

        return {
            "error": str(e)
        }


@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    updated_user: UserUpdate,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return {"error": "User not found"}

    user.name = updated_user.name
    user.email = updated_user.email

    db.commit()
    db.refresh(user)

    return {
        "message": "User updated successfully"
    }


@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return {"error": "User not found"}

    db.delete(user)
    db.commit()

    return {
        "message": "User deleted successfully"
    }
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from schemas import UserBase
from db.models import Users

def create_user(db: Session, request: UserBase):
    new_user = Users(
        username = request.username,
        password = request.password,
        email = request.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(Users).all()

def get_user_by_username(db: Session, username: str):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with username {username} not found.",
        )
    return user

def update_user(db: Session, id: int, request: UserBase):
    user = db.query(Users).filter(Users.id == id)
    user.update({
        Users.username: request.username,
        Users.email: request.email,
        Users.password: request.password
    })
    db.commit()
    return 'ok'

def delete_user(db: Session, id: int):
    user = db.query(Users).filter(Users.id == id).first()
    db.delete(user)
    db.commit()
    return 'dlete ok'
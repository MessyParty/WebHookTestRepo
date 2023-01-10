from typing import List, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.depts import get_db
from app.crud import crud_user
from app.schemas.user import UserResponse, UserCreate

router = APIRouter()


@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    users = crud_user.user.get_users(db)
    return list(map(lambda user: UserResponse(nick_name=user.nick_name, email=user.email), users))


@router.post("/", response_model=UserResponse)
def create_user(
        *,
        db: Session = Depends(get_db),
        user_requests: UserCreate
) -> Any:
    user = crud_user.user.create_user(db, user_create=user_requests)
    return UserResponse(nick_name=user.nick_name, email=user.email)

from typing import Any

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud
from app.api.depts import get_db
from app.schemas.token import Token

router = APIRouter()


@router.post("/login/access-token", response_model=Token)
def login(
        db: Session = Depends(get_db),
        login_data: OAuth2PasswordRequestForm = Depends()
) -> Any:
    user = crud.user.authenticate(db, email=login_data.username, password=login_data.password)
    return crud.session.create_session(db, user=user)

# @router.delete("/logout", status_code=status.HTTP_204_NO_CONTENT)
# def logout(db: Session = Depends(get_db),
#            current_user: User = Depends(get_current_user)):
#     crud.session.delete_session(db, current_user=current_user)

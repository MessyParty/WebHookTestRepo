from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api.depts import get_db, get_current_user_authorizer

from app.models.user import User
from app.schemas.history import HistoryResponse

router = APIRouter()


@router.get("/")
def read_histories(
        *,
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100,
        current_user: User = Depends(get_current_user_authorizer())
) -> List[HistoryResponse]:
    histories = crud.history.get_histories(db, user_id=current_user.id, skip=skip, limit=limit)
    return list(map(lambda h: HistoryResponse(id=h.id, detail=h.detail, money=h.money,
                                              created_at=h.created_at,
                                              updated_at=h.updated_at), histories))

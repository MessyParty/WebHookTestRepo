from typing import List

from sqlalchemy.orm import Session

from app.models.history import History


class CRUDHistory:
    def get_histories(self, db: Session, *, user_id: int, skip: int = 0, limit: int = 100) -> List[History]:
        from app.models.user import User
        return db.query(History).outerjoin(User, User.id == History.user_id) \
            .filter(User.id == user_id) \
            .filter(History.is_deleted is False) \
            .offset(skip) \
            .limit(limit) \
            .all()


history = CRUDHistory()

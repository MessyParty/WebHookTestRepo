from fastapi import APIRouter

from app.api.api_v1.end_points import users, session, histories

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(session.router, tags=["login"])
api_router.include_router(histories.router, prefix="/histories", tags=["histories"])

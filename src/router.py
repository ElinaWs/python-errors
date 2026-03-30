from datetime import datetime

from fastapi import APIRouter
from .schema import UserSchema

user_router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@user_router.get("/<id>", response_model=UserSchema)
def get_user(id: int) -> UserSchema:
    return UserSchema(
        id=id,
        name="John Doe",
        age=17,
        gender="male",
        created_at=datetime(2020, 1, 1),
    )

@user_router.post("/")
def create(
    user: UserSchema,
):
    return user

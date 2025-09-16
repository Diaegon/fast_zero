from http import HTTPStatus
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.models import User
from fast_zero.routers import auth, users
from fast_zero.schemas import UserPublic

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)

SessionDep = Annotated[Session, Depends(get_session)]


@app.get('/users/{user_id}', response_model=UserPublic)
def read_user_with_id(user_id: int, session: SessionDep):
    user = session.scalar(select(User).where(User.id == user_id))
    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    return user

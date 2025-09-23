from typing import Annotated

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from fast_zero.database import get_session
from fast_zero.routers import auth, todos, users

app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)

SessionDep = Annotated[Session, Depends(get_session)]

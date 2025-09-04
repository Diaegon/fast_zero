from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


# modelo de dados que o usuario deve enviar para criar uma conta


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


# modelo de dados que será retornado para o cliente, sem senha.


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]

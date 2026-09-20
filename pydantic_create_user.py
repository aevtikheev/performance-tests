from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class CreateUserRequestSchema(BaseModel):
    """
    Структура данных запроса для создания нового пользователя.
    """
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema

from pydantic import BaseModel, EmailStr, Field, ConfigDict

from app.models.users import UserRole


class UserCreate(BaseModel):
    email: EmailStr = Field(description="Email пользователя")
    password: str = Field(
        min_length=8,
        description="Пароль (минимум 8 символов)"
    )


class User(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    is_admin: bool

    model_config = ConfigDict(from_attributes=True)


class AdminCreate(BaseModel):
    email: EmailStr = Field(description="Email пользователя")
    password: str = Field(
        min_length=8,
        description="Пароль (минимум 8 символов)"
    )
    role: UserRole = Field(default='admin')

    model_config = ConfigDict(from_attributes=True)
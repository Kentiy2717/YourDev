from datetime import datetime
from sqlalchemy import (
    JSON,
    String
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from your_dev.core.database import Base

from typing import Literal

UserRole = Literal['admin', 'customer']


class AdminProfile(Base):
    '''Модель для версионирования информации в профиле админа.'''

    __tablename__ = 'admin_profiles'

    id: Mapped[int] = mapped_column(primary_key=True)
    name_for_index: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(50))
    slogan: Mapped[str] = mapped_column(String(50))
    about: Mapped[str]
    stats: Mapped[dict] = mapped_column(JSON)
    contacts: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    is_active: Mapped[bool] = mapped_column(default=False)


class User(Base):
    '''Общая модель пользователя.'''

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True
    )
    last_name: Mapped[str | None] = mapped_column(String(50))
    first_name: Mapped[str] = mapped_column(String(50))
    middle_name: Mapped[str | None] = mapped_column(String(50))
    password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    role: Mapped[UserRole] = mapped_column(default='customer')
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())

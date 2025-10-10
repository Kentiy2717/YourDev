from sqlalchemy import JSON, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from your_dev.core.database import Base

from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    pass

# !!!!           ЭТО ТОЛЬКО НАБРОСОК            !!!!
# !!!!  НУЖНО ПРОДУМАТЬ И ДОДЕЛАТЬ РЕАЛИЗАЦИЮ   !!!!

UserRole = Literal['admin', 'customet', 'observer']


class User(Base):

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    role: Mapped[UserRole] = mapped_column(default='observer')
    contacts: Mapped[dict | None] = mapped_column(JSON)


class Admin(User):

    __tablename__ = 'admin'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    name: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(50))
    slogan: Mapped[str] = mapped_column(String(50))
    about: Mapped[str]
    stats: Mapped[dict] = mapped_column(JSON)


class Customer(User):

    __tablename__ = 'customer'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    middle_name: Mapped[str] = mapped_column(String(50))
    company_name: Mapped[str] = mapped_column(String(50))
    notes: Mapped[str]
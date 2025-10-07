from sqlalchemy import JSON, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, index=True)
    name: Mapped[str] = mapped_column(String(50))
    is_active: Mapped[bool] = mapped_column(default=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    name: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(50))
    slogan: Mapped[str] = mapped_column(String(50))
    about: Mapped[str]
    stats: Mapped[dict] = mapped_column(JSON)
    contacts: Mapped[dict] = mapped_column(JSON)
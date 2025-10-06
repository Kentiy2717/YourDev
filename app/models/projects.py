from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, index=True)
    is_active: Mapped[bool] = mapped_column(default=True)
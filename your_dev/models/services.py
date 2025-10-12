from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from your_dev.core.database import Base


class Service(Base):
    __tablename__ = 'services'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str]
    price: Mapped[str] = mapped_column(String(20))
    features: Mapped[list[str]] = mapped_column(JSON, default=list)
    process: Mapped[list[str] | None] = mapped_column(JSON, default=list)
    technologies: Mapped[list[str] | None] = mapped_column(JSON, default=list)
    cta: Mapped[str] = mapped_column(String(50), unique=True)
    icon: Mapped[str] = mapped_column(String(50), unique=True)
    highlight: Mapped[bool]
    is_active: Mapped[bool] = mapped_column(default=True)
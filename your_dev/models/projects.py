from datetime import datetime
from sqlalchemy import JSON, ForeignKey, SmallInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from your_dev.core.database import Base

from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    pass

Badge = Literal[
    'УЧЕБНЫЙ',
    'ЛИЧНЫЙ ПРОЕКТ',
    'НА ЗАКАЗ',
    'OPEN SOURCE',
    'INDUSTRY'
]

Status = Literal[
    'Завершен',
    'Онлайн',
    'В работе',
    'Внедрен в производство',
    'Онлайн на хосте заказчика'
]

ComplexityLevel = Literal[1, 2, 3, 4, 5]


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(primary_key=True)
    name_project: Mapped[str] = mapped_column(String(100), index=True)
    title: Mapped[str] = mapped_column(unique=True)
    badge: Mapped[Badge] = mapped_column(default='ЛИЧНЫЙ ПРОЕКТ')
    description: Mapped[str]
    long_description: Mapped[str]
    highlights: Mapped[list[str]] = mapped_column(JSON, default=list)
    technologies: Mapped[list[str]] = mapped_column(JSON, default=list)
    github_url: Mapped[str] = mapped_column(String(200), nullable=True)
    demo_url: Mapped[str] = mapped_column(String(200), nullable=True)
    status: Mapped[Status] = mapped_column(default='Онлайн', index=True)
    complexity: Mapped[ComplexityLevel] = mapped_column(SmallInteger, default=1)
    automation_level: Mapped[int] = mapped_column(SmallInteger, default=0)
    metrics: Mapped[dict] = mapped_column(JSON)
    is_active: Mapped[bool] = mapped_column(default=False, index=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
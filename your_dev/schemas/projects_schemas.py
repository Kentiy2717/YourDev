from pydantic import (
    BaseModel,
    ConfigDict,
    HttpUrl,
    UrlConstraints,
    Field
)

from your_dev.models.projects import Badge, ComplexityLevel, Status


class Project(BaseModel):
    '''Модель для ответа с данными проекта.
    Используется в GET-запросах.'''

    name_project: str = Field(max_length=100)
    title: str = Field(description="Уникальное название для URL")
    badge: Badge = Field(default='ЛИЧНЫЙ ПРОЕКТ')
    description: str
    long_description: str
    highlights: list[str] = Field(default_factory=list)
    technologies: list[str] = Field(default_factory=list)
    github_url: HttpUrl | None = Field(max_length=200)
    demo_url: HttpUrl | None = Field(max_length=200)
    status: Status = Field(default='Онлайн')
    complexity: ComplexityLevel = Field(default=1, ge=1, le=5)
    automation_level: int = Field(default=0, ge=0, le=100)
    metrics: dict = Field(default_factory=dict)
    is_active: bool = Field(default=False)

    model_config = ConfigDict(from_attributes=True)


class ProjectCreate(BaseModel):
    '''Модель для создания и обновления данных проекта.
    Используется в GET-запросах.'''

    name_project: str = Field(max_length=100)
    title: str = Field(description="Уникальное название для URL")
    badge: Badge = Field(default='ЛИЧНЫЙ ПРОЕКТ')
    description: str
    long_description: str
    highlights: list[str] = Field(default_factory=list)
    technologies: list[str] = Field(default_factory=list)
    github_url: HttpUrl | None = Field(max_length=200)
    demo_url: HttpUrl | None = Field(max_length=200)
    status: Status = Field(default='Онлайн')
    complexity: ComplexityLevel = Field(default=1, ge=1, le=5)
    automation_level: int = Field(default=0, ge=0, le=100)
    metrics: dict = Field(default_factory=dict)
    is_active: bool = Field(default=False)
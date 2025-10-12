from pydantic import (
    BaseModel,
    ConfigDict,
    HttpUrl,
    Field
)

from your_dev.models.projects import Badge, ComplexityLevel, Status


class Project(BaseModel):
    '''Модель для ответа с данными проекта.
    Используется в GET-запросах.'''

    name_project: str = Field(description='Уникальное наименование проекта')
    title: str = Field(description='Уникальное название проекта')
    badge: Badge = Field(
        description=('Бэйдж - "УЧЕБНЫЙ", "ЛИЧНЫЙ ПРОЕКТ", "НА ЗАКАЗ", '
                     '"OPEN SOURCE", "INDUSTRY"')
    )
    description: str = Field(description='Короткое описание проекта')
    long_description: str = Field(description='Полное описание проекта')
    highlights: list[str] = Field(description='Особенности проекта')
    technologies: list[str] = Field(description='Список используемых технологий')
    github_url: HttpUrl | None = Field(description='Ссылка на GitHub проекта')
    demo_url: HttpUrl | None = Field(description='Ссылка на проект')
    status: Status = Field(
        description=('Статус - "Завершен", "Онлайн", "В работе", '
                     '"Внедрен в производство", "Онлайн на хосте заказчика"')
    )
    complexity: ComplexityLevel = Field(description='Сложность от 1 до 5')
    automation_level: int = Field(description='Уровень автоматизации')
    metrics: dict = Field(description='Краткое резюме проекта')
    is_active: bool = Field(description='Отображение проекта на сайте')

    model_config = ConfigDict(from_attributes=True)


class ProjectCreate(BaseModel):
    '''Модель для создания и обновления данных проекта.
    Используется в POST и PUT запросах.'''

    name_project: str = Field(
        description='Уникальное наименование проекта',
        max_length=100
    )
    title: str = Field(description='Уникальное название проекта')
    badge: Badge = Field(
        description=('Бэйдж - "УЧЕБНЫЙ", "ЛИЧНЫЙ ПРОЕКТ", "НА ЗАКАЗ", '
                     '"OPEN SOURCE", "INDUSTRY"'),
        default='ЛИЧНЫЙ ПРОЕКТ'
    )
    description: str = Field(description='Короткое описание проекта')
    long_description: str = Field(description='Полное описание проекта')
    highlights: list[str] = Field(
        description='Особенности проекта',
        default_factory=list
    )
    technologies: list[str] = Field(
        description='Список используемых технологий',
        default_factory=list
    )
    github_url: HttpUrl | None = Field(
        description='Ссылка на GitHub проекта',
        max_length=200
    )
    demo_url: HttpUrl | None = Field(
        description='Ссылка на проект',
        max_length=200
    )
    status: Status = Field(
        description=('Статус - "Завершен", "Онлайн", "В работе", '
                     '"Внедрен в производство", "Онлайн на хосте заказчика"'),
        default='Онлайн'
    )
    complexity: ComplexityLevel = Field(
        description='Сложность от 1 до 5',
        default=1,
        ge=1, le=5
    )
    automation_level: int = Field(
        description='Уровень автоматизации',
        default=0,
        ge=0,
        le=100
    )
    metrics: dict = Field(
        description='Краткое резюме проекта',
        default_factory=dict
    )
    is_active: bool = Field(
        description='Отображение проекта на сайте',
        default=False
    )
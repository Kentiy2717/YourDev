from pydantic import (
    BaseModel,
    ConfigDict,
    Field
)


class Service(BaseModel):
    '''Модель для ответа с данными услуг.
    Используется в GET-запросах.'''

    title: str = Field(description='Уникальное название услуги')
    description: str = Field(description='Описание услуги')
    price: str = Field(description='Цена услуги')
    features: list[str] = Field(description='Особенности')
    process: list[str | None] = Field(description='Процесс разработки')
    technologies: list[str] = Field(description='Технологии')
    cta: str = Field(description='Уникальный призыв к действию')
    icon: str = Field(description='Уникальная иконка услуги')
    highlight: bool = Field(description='Метка популярной услуги')
    is_active: bool = Field(description='Отображение услуги на сайте')

    model_config = ConfigDict(from_attributes=True)


class ServiceCreate(BaseModel):
    '''Модель для создания и обновления данных услуги.
    Используется в POST и PUT запросах.'''

    title: str = Field(
        max_length=50,
        description='Уникальное название услуги'
    )
    description: str = Field(description='Описание услуги')
    price: str = Field(
        max_length=20,
        description='Цена услуги'
    )
    features: list[str] = Field(
        description='Особенности',
        default_factory=list
    )
    process: list[str | None] = Field(
        description='Процесс разработки',
        default_factory=list
    )
    technologies: list[str] = Field(
        description='Технологии',
        default_factory=list
    )
    cta: str = Field(
        max_length=50,
        description='Уникальный призыв к действию'
    )
    icon: str = Field(
        max_length=50,
        description='Уникальная иконка услуги'
    )
    highlight: bool = Field(
        default=False,
        description='Метка популярной услуги'
    )
    is_active: bool = Field(
        description='Отображение услуги на сайте',
        default=False
    )
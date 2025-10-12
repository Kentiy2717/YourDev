from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    SecretStr
)


class User(BaseModel):
    '''Модель для ответа с данными пользователя.
    Используется в GET-запросах.'''

    id: int = Field(description='Уникальный идентификатор категории')
    email: EmailStr = Field(description='email')
    last_name: str = Field(description='Фамилия')
    first_name: str = Field(description='Имя')
    middle_name: str = Field(description='Отчество')
    is_active: bool = Field(description='Активность пользователя')

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    '''Модель для создания и обновления данных пользователя.
    Используется в POST и PUT запросах.'''

    email: EmailStr = Field(description='Email пользователя')
    last_name: str = Field(
        max_length=50,
        description='Фамилия (необязательное поле)'
    )
    first_name: str = Field(
        max_length=50,
        description='Имя (обязательное поле)'
    )
    middle_name: str = Field(
        max_length=50,
        description='Отчество (необязательное поле)'
    )
    password: SecretStr = Field(
        min_length=8,
        description='Пароль (минимум 8 символов)'
    )


class AdminProfile(BaseModel):
    name_for_index: str = Field(description='Имя для отображения на главной странице')
    title: str = Field(description='Заголовок')
    slogan: str = Field(description='Слоган')
    about: str = Field(description='Обо мне')
    stats: dict = Field(description='Статы')
    contacts: dict = Field(description='Контакты')
    is_active: bool = Field(description='Активность профиля')

    model_config = ConfigDict(from_attributes=True)


class AdminProfileCreate(BaseModel):
    name_for_index: str = Field(description='Имя для отображения на главной странице')
    title: str = Field(description='Заголовок')
    slogan: str = Field(description='Слоган')
    about: str = Field(description='Обо мне')
    stats: dict = Field(description='Статы')
    contacts: dict = Field(description='Контакты')
    is_active: bool = Field(description='Активность профиля')
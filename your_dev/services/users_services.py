'''
Тут будет реализовано кэширование информации о профиле автора сайта
Нужно будет настроить возможность версионирования информации на главной
странице. Т.е. каждая строка в таблице admin это отображения опыта работы
автора в данный момент времени. Можно всегда создать обновление (новая строка),
а также вернуть данные из старых записей.
'''
from fastapi import HTTPException, status
from your_dev.repositories.users_repository import (
    AdminProfileRepository,
    UserRepository
)
from your_dev.schemas.users_schemas import (
    AdminProfile,
    AdminProfileCreate,
    User
)


class UserService:
    '''Сервисный класс для работы с профилями пользователей.'''

    def __init__(self, user_repo: UserRepository):
        self._user_repo = user_repo

    async def get_user_by_id(self, user_id: int) -> User:
        '''Получение пользователя по ID.'''

        user = await self._user_repo.get_by_id(user_id)
        return user

    async def get_admin(self) -> User:
        '''Возвращает пользователся с ролью "admin"'''

        admin = await self._user_repo.get_admin()
        return admin

    async def register_user(self, user_data: dict) -> User:
        '''Регистрация нового пользователя'''
####
        # Проверяем, не существует ли уже пользователь с таким email
        existing_user = await self._user_repo.get_by_email(user_data['email'])
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Пользователь с таким email уже существует"
            )
        return await self._user_repo.create_user(user_data)

    async def authenticate_user(self, email: str, password: str) -> User | None:
        '''Аутентификация пользователя.'''

        user = await self._user_repo.authenticate_user(email, password)
        if user.is_active:
            return user


class AdminProfileService:
    '''Сервисный класс для работы с профилями админа.'''

    def __init__(
        self,
        user_repo: UserRepository,
        profile_repo: AdminProfileRepository
    ):
        self._user_repo = user_repo
        self._profile_repo = profile_repo

    async def get_active_profile(self) -> AdminProfile:
        '''Возвращает профиль админа или создает его при первом обращении,
        если еще не создан.'''

        # Получаем профиль из репозитория, если админ уже создан.
        active_profile = await self._profile_repo.get_active_profile()
        return active_profile

    async def create_profile(self, profile_data: AdminProfileCreate) -> AdminProfile:
        '''Создает профиль админа и возвращает его.'''

        await self._validate_is_active_profile(is_active=profile_data.is_active)
        new_profile = await self._profile_repo.create_profile(profile_data)
        return new_profile

    async def _validate_is_active_profile(self, is_active: bool):
        '''Деактивирует текущий активный профиль и активирует переданный.'''

        if is_active:
            active_profile = self._profile_repo.get_active_profile()
            if active_profile is not None:
                active_profile.is_active = False

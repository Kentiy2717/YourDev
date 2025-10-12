'''
Тут будет реализовано кэширование информации о профиле автора сайта
Нужно будет настроить возможность версионирования информации на главной
странице. Т.е. каждая строка в таблице admin это отображения опыта работы
автора в данный момент времени. Можно всегда создать обновление (новая строка),
а также вернуть данные из старых записей.
'''

import os
from typing import TYPE_CHECKING

from sqlalchemy import select

from your_dev.core.auth import hash_password
from your_dev.core.initial_data import INITIAL_PROFILE_DATA
from your_dev.core.logger import logger
from your_dev.repositories.users_repository import (
    AdminProfileRepository,
    UserRepository
)
from your_dev.schemas.users_schemas import (
    AdminProfile,
    AdminProfileCreate,
    User,
    UserCreate
)


if TYPE_CHECKING:
    pass


class InitialService:
    '''Сервисный класс для создания стартовых проектов.'''


class UserService:
    '''Сервисный класс для работы с профилями пользователей.'''

    def __init__(self, user_repo: UserRepository):
        self._user_repo = user_repo

    async def get_admin(self) -> User:
        admin = await self._user_repo.get_admin()
        return admin


class AdminProfileService:
    '''Сервисный класс для работы с профилями админа.'''

    def __init__(
        self,
        user_repo: UserRepository,
        profile_repo: AdminProfileRepository
    ):
        self._user_repo = user_repo
        self._profile_repo = profile_repo

    async def _create_account_and_profile_admin_when_initial_app(self) -> None:
        '''Создает учетную запить и профиль админа,
        при первом обращении за ним.'''

        admin = await self._user_repo.get_admin()
        if admin is None:

            # Создаем стартовую учетную запись админа.
            await self._user_repo.create_user(
                user_data=dict(
                    email=os.getenv('INITIAL_ADMIN_EMAIL'),
                    last_name='Мотрий',
                    first_name='Иннокентий',
                    middle_name='Александрович',
                    password=hash_password(os.getenv('INITIAL_ADMIN_PASSWORD')),
                    role='admin'
                )
            )

            # Создаем стартовый профиль админа.
            initial_profile = await self._profile_repo.create_profile(
                profile_data=dict(
                    name_for_index=INITIAL_PROFILE_DATA['name'],
                    title=INITIAL_PROFILE_DATA['title'],
                    slogan=INITIAL_PROFILE_DATA['slogan'],
                    about=INITIAL_PROFILE_DATA['about'],
                    stats=INITIAL_PROFILE_DATA['stats'],
                    contacts=INITIAL_PROFILE_DATA['contacts'],
                    is_active=True,
                )
            )
        logger.info('✅ Админ успешно создан со стартовыми настройками.')
        return initial_profile

    async def get_active_profile(self) -> AdminProfile:
        '''Возвращает профиль админа или создает его при первом обращении,
        если еще не создан.'''

        # Получаем профиль из репозитория, если админ уже создан.
        active_profile = await self._profile_repo.get_active_profile()

        # Если админ еще не создан, то создаем стартовый аккаунт и профиль.
        if active_profile is None:
            active_profile = await self._create_account_and_profile_admin_when_initial_app()
        return active_profile

    async def create_profile(self, profile_data: AdminProfileCreate) -> AdminProfile:
        # Проверка что user - admin (РАЗКОМЕНТИТЬ, КОГДА СДЕЛАЮ АВТОРИЗАЦИЮ)
        # await self._validate_user_role(user_id=user_id)
        await self._validate_is_active_profile(is_active=profile_data.is_active)
        new_profile = await self._profile_repo.create_profile(profile_data)
        return new_profile

    async def _validate_is_active_profile(self, is_active: bool):
        '''Деактивирует текущий активный профиль и активирует переданный.'''

        if is_active:
            active_profile = self._profile_repo.get_active_profile()
            if active_profile is not None:
                active_profile.is_active = False

    # Проверка что user - admin (РАЗКОМЕНТИТЬ, КОГДА СДЕЛАЮ АВТОРИЗАЦИЮ)
    '''async def _validate_user_role(self, user_id):
        /'/'/'Вызывает исключение, если запрос не от админа./'/'/'

        from sqlalchemy.orm import object_session
        session = object_session(self)

        if session:
            user = await session.scalar(select(User)
                                        .where(User.id == user_id))
            if user and user.role != 'admin':
                raise ValueError(
                    'AdminProfile может быть связан только с '
                    'пользователями с правами администратора'
                )'''

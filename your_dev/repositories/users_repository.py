from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from your_dev.models.users import AdminProfile, User


class UserRepository:
    '''Репозиторий для работы с моделями пользователей.'''

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(self, email: str) -> User | None:
        '''Возвращает пользователя по его email.'''

        user = await self.db.scalar(
            select(User).where(User.email == email, User.is_active)
        )
        return user

    async def get_admin(self) -> User | None:
        '''Возвращает админа.'''

        admin = await self.db.scalar(
            select(User).where(User.role == 'admin', User.is_active)
        )
        return admin

    async def get_all_users(self) -> list[User]:
        '''Возвращает всех пользователей. Используется в админке.'''

        users_query = await self.db.scalars(select(User))
        return users_query.all()

    async def create_user(self, user_data: dict) -> User:
        '''Создает пользователя.'''

        user = User(**user_data)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user


class AdminProfileRepository:
    '''Репозиторий для работы с профилями админа.'''

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, profile_id: int) -> AdminProfile | None:
        '''Возвращает профиль по id. Используется в админке.'''

        profile = await self.db.scalar(select(AdminProfile)
                                       .where(AdminProfile.id == profile_id))
        return profile

    async def get_active_profile(self) -> AdminProfile | None:
        '''Возвращает все профили.'''

        profile = await self.db.scalar(select(AdminProfile)
                                       .where(AdminProfile.is_active))
        return profile

    async def get_all_profiles(self) -> list[AdminProfile]:
        '''Возвращает все профили. Используется в админке.'''

        profiles_query = await self.db.scalars(select(AdminProfile))
        return profiles_query.all()

    async def create_profile(self, profile_data: dict) -> AdminProfile:
        '''Создает новый профиль. Используется в админке.'''

        profile = AdminProfile(**profile_data)
        self.db.add(profile)
        await self.db.commit()
        await self.db.refresh(profile)
        return profile

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from your_dev.models.users import AdminProfile, User


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, user_id: int) -> User | None:
        user = await self.db.scalar(select(User).where(User.id == user_id,
                                                       User.is_active))
        return user

    async def get_by_email(self, email: str) -> User | None:
        user = await self.db.scalar(select(User).where(User.email == email,
                                                       User.is_active))
        return user

    async def get_admin(self) -> User | None:
        user = await self.db.scalar(select(User)
                                    .where(User.role == 'admin',
                                           User.is_active))
        return user

    async def get_all_users(self) -> list[User]:
        users_query = await self.db.scalars(select(User))
        return users_query.all()

    async def create_user(self, user_data: dict) -> User:
        user = User(**user_data)
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        return user


class AdminProfileRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, profile_id: int) -> AdminProfile | None:
        profile = await self.db.scalar(select(AdminProfile)
                                       .where(AdminProfile.id == profile_id))
        return profile

    async def get_active_profile(self) -> AdminProfile | None:
        profile = await self.db.scalar(select(AdminProfile)
                                       .where(AdminProfile.is_active))
        return profile

    async def get_all_profiles(self) -> list[AdminProfile]:
        profiles_query = await self.db.scalars(select(AdminProfile))
        return profiles_query.all()

    async def create_profile(self, profile_data: dict) -> AdminProfile:
        profile = AdminProfile(**profile_data)
        self.db.add(profile)
        await self.db.commit()
        await self.db.refresh(profile)
        return profile

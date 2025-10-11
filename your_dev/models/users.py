from datetime import datetime
from sqlalchemy import (
    ForeignKey,
    String,
    select
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    validates,
    relationship
)

from your_dev.core.database import Base

from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    pass

UserRole = Literal['admin', 'customer', 'observer']


class User(Base):
    '''Общая модель пользователя.'''

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True
    )
    first_name: Mapped[str] = mapped_column(String(50))
    middle_name: Mapped[str | None] = mapped_column(String(50))
    last_name: Mapped[str | None] = mapped_column(String(50))
    hashed_password: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    role: Mapped[UserRole] = mapped_column(default='customer')
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())

    admin_profiles: Mapped[list['AdminProfile']] = relationship(
        back_populates='user',
        cascade='all, delete-orphan'
    )

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError('Invalid email address')
        return email


class AdminProfile(Base):
    '''Модель для версионирования информации в профиле админа.'''

    __tablename__ = 'admin_profile'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    name_for_index: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(50))
    slogan: Mapped[str] = mapped_column(String(50))
    about: Mapped[str] 
    stats: Mapped[dict]
    contacts: Mapped[dict]
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    is_active: Mapped[bool] = mapped_column(default=True)

    user: Mapped['User'] = relationship(back_populates='admin_profile')

    @validates('user_id')
    async def validate_user_role(self, key, user_id):
        '''Вызывает исключение, если запрос не от админа.'''

        from sqlalchemy.orm import object_session
        session = object_session(self)

        if session:
            user = await session.scalar(select(User)
                                        .where(User.id == user_id))
            if user and user.role != 'admin':
                raise ValueError(
                    'AdminProfile может быть связан только с '
                    'пользователями с правами администратора'
                )
        return user_id

    @validates('is_active')
    async def validate_user_role(self, key, is_active):
        '''Если мы добавили профиль, который хотим активировать сразу,
        то сначала неактивируем текущий активный профиль.'''

        from sqlalchemy.orm import object_session
        session = object_session(self)

        if session and is_active:
            active_profile = await session.scalar(
                select(AdminProfile).where(AdminProfile.is_active)
            )
            if active_profile is not None:
                active_profile.is_active = False
        return is_active

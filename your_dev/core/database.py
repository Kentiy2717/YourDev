from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession
)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase

from your_dev.core.config import settings
from your_dev.core.logger import logger

async_engine = create_async_engine(settings.DATABASE_URL)

async_session_maker = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)


class Base(DeclarativeBase):
    pass


async def get_async_db() -> AsyncGenerator[AsyncSession, None]:
    '''
    Асинхронно предоставляет сессию SQLAlchemy для работы с PostgreSQL.

    Особенности:
    - Гарантирует закрытие сессии даже при возникновении исключений
    - Логирует возникающие ошибки

    Yields:
        AsyncSession: Асинхронная сессия для работы с базой данных
    '''

    async with async_session_maker() as session:

        try:
            yield session
        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка в бизнес-логике: {e}")
            await session.rollback()
            raise

        except Exception as e:
            logger.error(f"❌ Неожиданная ошибка: {e}")
            await session.rollback()
            raise

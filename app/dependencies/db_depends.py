import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from typing import AsyncGenerator

from app.database import async_session_maker

logger = logging.getLogger(__name__)


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

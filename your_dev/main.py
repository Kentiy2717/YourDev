from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from sqlalchemy.exc import SQLAlchemyError

from your_dev.core.database import async_session_maker
from your_dev.core.logger import logger
from your_dev.repositories.service_repository import ServiceRepository
from your_dev.repositories.users_repository import (
    AdminProfileRepository,
    UserRepository
)
from your_dev.repositories.projects_repository import ProjectRepository
from your_dev.repositories.users_repository import UserRepository
from your_dev.routers import (
    auth_routers,
    main_routers,
    projects_routers,
    services_routers
)
from your_dev.services.initialization_services import InitializationService


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Starting initialization...")

    # Создаем сервис инициализации.
    async with async_session_maker() as session:
        try:

            initialization_service = InitializationService(
                user_repo=UserRepository(session),
                profile_repo=AdminProfileRepository(session),
                project_repo=ProjectRepository(session),
                service_repo=ServiceRepository(session),
            )
            await initialization_service.create_admin_if_not_exist()
            await initialization_service.create_profile_if_not_exist()
            # await initialization_service.create_projects_if_not_exist()
            # await initialization_service.create_services_if_not_exist()
            print("✅ Initialization completed!")

            await session.commit()
        except SQLAlchemyError as e:
            logger.error(f"❌ Ошибка в бизнес-логике: {e}")
            await session.rollback()
            raise
        except Exception as e:
            logger.error(f"❌ Неожиданная ошибка: {e}")
            await session.rollback()
            raise

    yield

    # Shutdown
    print("👋 Shutting down...")

app = FastAPI(
    title='🌎 YOUR PYTHON DEV',
    description='Python Full-Stack Developer Portfolio',
    version='1.0.0',
    lifespan=lifespan
)

app.mount('/static', StaticFiles(directory='your_dev/static'), name='static')

# app.include_router(auth_routers.router)
app.include_router(projects_routers.router)
app.include_router(services_routers.router)
app.include_router(main_routers.router)


@app.get('/')
async def root():
    '''Корневой маршрут, подтверждающий, что API работает.'''

    return {'message': 'Добро пожаловать в API сервиса YourDev!'}

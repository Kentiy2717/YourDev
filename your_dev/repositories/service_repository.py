from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from your_dev.models.services import Service


class ServiceRepository:
    '''Репозиторий для работы с услугами админа.'''

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_service_by_title(self, title: str) -> Service:
        '''Возвращает услугу про его title. Используется в админке.'''

        service = await self.db.scalar(
            select(Service).where(Service.title == title)
        )
        return service

    async def get_all_active_services(self) -> list[Service]:
        '''Возвращает все активные услуги.'''

        services_query = await self.db.scalars(
            select(Service).where(Service.is_active)
        )
        return services_query.all()

    async def get_all_services(self) -> list[Service]:
        '''Возвращает все услуги. Используется в админке.'''

        services_query = await self.db.scalars(select(Service))
        return services_query.all()

    async def create_service(self, service_data: dict) -> Service:
        '''Создает новый услугу и возвращает его.'''

        service = Service(**service_data)
        self.db.add(service)
        await self.db.commit()
        await self.db.refresh(service)
        return service

    async def delete_service(self, title: str) -> None:
        '''Логическое удаление проекта.'''

        service = await self.db.scalar(
            select(Service).where(Service.id == title)
        )
        service.is_active = False
        await self.db.commit()
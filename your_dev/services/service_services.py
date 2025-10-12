from your_dev.models.services import Service
from your_dev.repositories.service_repository import ServiceRepository
from your_dev.schemas.services_schemas import ServiceCreate


class ServiceService:
    '''Сервисный класс для работы с услугами админа.'''

    def __init__(self, service_repo: ServiceRepository):
        self._service_repo = service_repo

    async def get_service_by_title(self, title: str) -> Service | None:
        '''Возвращает активный проект по его имени. Используется в админке'''

        # Получаем проект из репозитория.
        service = await self._service_repo.get_service_by_title(title)
        return service

    async def get_all_active_services(self) -> list[Service]:
        '''Возвращает все активные услуги.'''

        services = await self._service_repo.get_all_active_services()
        return services

    async def get_all_services(self) -> list[Service]:
        '''Возвращает все услуги. Используется в админке.'''

        # Получаем проект из репозитория.
        services = await self._service_repo.get_all_services()
        return services

    async def create_service(self, service_data: ServiceCreate) -> Service:
        '''Cоздает услугу. Используется в админке.'''

        # Проверка что service - service (РАЗКОМЕНТИТЬ, КОГДА СДЕЛАЮ АВТОРИЗАЦИЮ)
        # await self._validate_service_role(service_id=service_id)
        new_service = await self._service_repo.create_service(service_data)
        return new_service
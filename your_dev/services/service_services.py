from your_dev.core.initial_data import INITIAL_PROJECTS_DATA
from your_dev.core.logger import logger
from your_dev.repositories.service_repository import ServiceRepository
# from your_dev.schemas.services_schemas import Service, ServiceCreate


class ServiceService:
    '''Сервисный класс для работы с услугами админа.'''

    def __init__(self, service_repo: ServiceRepository):
        self._service_repo = service_repo
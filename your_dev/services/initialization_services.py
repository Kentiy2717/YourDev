from your_dev.repositories.service_repository import ServiceRepository
from your_dev.repositories.users_repository import (
    AdminProfileRepository,
    UserRepository
)
from your_dev.repositories.projects_repository import ProjectRepository


class InitializationService:
    '''Сервисный класс для работы с профилями админа.'''

    def __init__(
        self,
        user_repo: UserRepository,
        profile_repo: AdminProfileRepository,
        project_repo: ProjectRepository,
        service_repo: ServiceRepository
    ):
        self._user_repo = user_repo
        self._profile_repo = profile_repo
        self._project_repo = project_repo
        self._service_repo = service_repo
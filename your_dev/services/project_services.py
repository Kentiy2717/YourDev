from your_dev.repositories.projects_repository import ProjectRepository
from your_dev.schemas.projects_schemas import Project, ProjectCreate


class ProjectService:
    '''Сервисный класс для работы с профилями админа.'''

    def __init__(self, project_repo: ProjectRepository):
        self._project_repo = project_repo

    async def get_active_project_by_name_project(self, name_project: str) -> Project | None:
        '''Возвращает активный проект по его имени.'''

        # Получаем проект из репозитория.
        project = await self._project_repo.get_active_project_by_name_project(name_project)
        return project

    async def get_all_active_projects(self) -> list[Project]:
        '''Возвращает все активные проекты.'''

        projects = await self._project_repo.get_all_active_projects()
        return projects

    async def get_all_projects(self) -> list[Project]:
        '''Возвращает все проекты. Используется в админке.'''

        # Получаем проект из репозитория.
        projects = await self._project_repo.get_all_projects()
        return projects

    async def create_project(self, project_data: ProjectCreate) -> Project:
        '''Cоздает проект. Используется в админке.'''

        # Проверка что project - project (РАЗКОМЕНТИТЬ, КОГДА СДЕЛАЮ АВТОРИЗАЦИЮ)
        # await self._validate_project_role(project_id=project_id)
        new_project = await self._project_repo.create_project(project_data)
        return new_project

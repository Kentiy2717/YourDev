from your_dev.core.initial_data import INITIAL_PROJECTS_DATA
from your_dev.core.logger import logger
from your_dev.repositories.projects_repository import ProjectRepository
from your_dev.schemas.projects_schemas import Project, ProjectCreate


class ProjectService:
    '''Сервисный класс для работы с профилями админа.'''

    def __init__(self, project_repo: ProjectRepository):
        self._project_repo = project_repo

    async def _create_projects_when_initial_app(self) -> None:
        '''Создает стартовые проекты, при первом обращении за ним.'''

        initial_projects = []
        for project_data in INITIAL_PROJECTS_DATA:

            # Создаем стартовые проекты.
            initial_project = await self._project_repo.create_project(
                profile_data=dict(
                    name_project=project_data['name_project'],
                    title=project_data['title'],
                    badge=project_data['badge'],
                    description=project_data['description'],
                    long_description=project_data['long_description'],
                    highlights=project_data['highlights'],
                    technologies=project_data['technologies'],
                    github_url=project_data['github_url'],
                    demo_url=project_data['demo_url'],
                    status=project_data['status'],
                    complexity=project_data['complexity'],
                    automation_level=project_data['automation_level'],
                    metrics=project_data['metrics'],
                    is_active=True,
                )
            )
            logger.info(
                f'✅ Стартовый проект ({INITIAL_PROJECTS_DATA['title']}) '
                'успешно создан.'
            )
            initial_projects.append(initial_project)
        return initial_projects

    async def get_all_active_projects(self) -> list[Project]:
        '''Возвращает все проекты. Если нет ни одного проекта (при первом
        обращении), то создает их.'''

        projects = await self._project_repo.get_all_active_projects()
        return projects

    async def get_all_projects(self) -> list[Project]:
        '''Возвращает все проекты. Если нет ни одного проекта (при первом
        обращении), то создает их.'''

        # Получаем проект из репозитория.
        projects = await self._checking_profile_existence_and_get_project()

        # Если проектов еще нет, то создаем стартовые проекты.
        if projects is None:
            projects = await self._create_projects_when_initial_app()
        return projects

    async def create_profile(self, profile_data: ProjectCreate) -> Project:
        # Проверка что project - project (РАЗКОМЕНТИТЬ, КОГДА СДЕЛАЮ АВТОРИЗАЦИЮ)
        # await self._validate_project_role(project_id=project_id)
        await self._validate_is_active_profile(is_active=profile_data.is_active)
        new_profile = await self._profile_repo.create_profile(profile_data)
        return new_profile

    async def _checking_profile_existence(self):
        '''Проверяет существуют ли проекты, создает их если нет и возвращает.'''

        # Получаем проект из репозитория.
        projects = await self._project_repo.get_all_projects()

        # Если проектов еще нет, то создаем стартовые проекты.
        if projects is None:
            projects = await self._create_projects_when_initial_app()
        return projects

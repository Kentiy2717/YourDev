import os

from your_dev.core.auth import hash_password
from your_dev.core.initial_data import (
    INITIAL_PROFILE_DATA,
    INITIAL_PROJECTS_DATA,
    INITIAL_SERVICES_DATA
)
from your_dev.core.logger import logger
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

    async def create_admin_if_not_exist(self) -> None:
        '''Создает учетную запить админа, если админа нет.'''

        admin = await self._user_repo.get_admin()
        if admin is None:

            # Создаем стартовую учетную запись админа.
            await self._user_repo.create_user(
                user_data=dict(
                    email=os.getenv('INITIAL_ADMIN_EMAIL'),
                    last_name='Мотрий',
                    first_name='Иннокентий',
                    middle_name='Александрович',
                    password=hash_password(os.getenv('INITIAL_ADMIN_PASSWORD')),
                    role='admin'
                )
            )
            logger.info('✅ Админ успешно создан со стартовыми настройками.')
        else:
            logger.info('💡 Админ уже существует.')

    async def create_profile_if_not_exist(self) -> None:
        '''Создает начальный профиль админа, если их нет.'''

        profiles = await self._profile_repo.get_all_profiles()
        if not profiles:

            # Создаем стартовый профиль.
            await self._profile_repo.create_profile(
                profile_data=dict(
                    name_for_index=INITIAL_PROFILE_DATA['name'],
                    title=INITIAL_PROFILE_DATA['title'],
                    slogan=INITIAL_PROFILE_DATA['slogan'],
                    about=INITIAL_PROFILE_DATA['about'],
                    stats=INITIAL_PROFILE_DATA['stats'],
                    contacts=INITIAL_PROFILE_DATA['contacts'],
                    is_active=True,
                )
            )
            logger.info('✅ Стартовый профиль создан успешно.')
        else:
            logger.info('💡 Профиль уже существует.')

    async def create_projects_if_not_exist(self) -> None:
        '''Создает начальные проекты админа, если их нет.'''

        for project_data in INITIAL_PROJECTS_DATA:
            project = await self._project_repo.get_by_name_project(
                name_project=project_data['name_project']
            )
            if not project:

                # Создаем стартовые проекты.
                await self._project_repo.create_project(
                    project_data=dict(
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
                    f'✅ Стартовые проект ({project_data["title"]}) '
                    'успешно создан.'
                )
            else:
                logger.info(
                    f'💡 Стартовый проект {project_data["title"]} '
                    'уже существует.'
                )

    async def create_services_if_not_exist(self) -> None:
        '''Создает начальные услуги админа, если их нет.'''

        for service_data in INITIAL_SERVICES_DATA:
            service = await self._service_repo.get_service_by_title(
                title=service_data['title']
            )
            if not service:

                # Создаем стартовые услуги.
                await self._service_repo.create_service(
                    service_data=dict(
                        title=service_data['title'],
                        description=service_data['description'],
                        price=service_data['price'],
                        features=service_data['features'],
                        process=service_data.get('process', []),
                        technologies=service_data['technologies'],
                        cta=service_data['cta'],
                        icon=service_data['icon'],
                        highlight=service_data['highlight'],
                        is_active=True,
                    )
                )
                logger.info(
                    f'✅ Стартовая услуга ({service_data["title"]}) '
                    'успешно создана.'
                )
            else:
                logger.info(
                    f'💡 Стартовая услуга {service_data["title"]} '
                    'уже существует.'
                )

    async def delete_all_projects(self) -> None:
        '''Для отладки.'''
        await self._project_repo.delete_all_project()

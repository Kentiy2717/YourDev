from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from your_dev.models.projects import Project


class ProjectRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_name_project(self, name_project: int) -> Project | None:
        '''Возвращает проект про его name_project. Используется в админке.'''

        project = await self.db.scalar(
            select(Project).where(Project.id == name_project)
        )
        return project

    async def get_is_active_project_by_name_project(
            self, name_project: int
    ) -> Project | None:
        '''Возвращает проект про его name_project если он активен.'''

        project = await self.db.scalar(
            select(Project).where(Project.id == name_project,
                                  Project.is_active)
        )
        return project

    async def get_all_active_projects(self) -> list[Project]:
        '''Возвращает все активные проекты.'''

        projects_query = await self.db.scalars(select(Project)
                                               .where(Project.is_active))
        return projects_query.all()

    async def get_all_projects(self) -> list[Project]:
        '''Возвращает все проекты. Используется в админке.'''

        projects_query = await self.db.scalars(select(Project))
        return projects_query.all()

    async def create_project(self, project_data: dict) -> Project:
        '''Создает новый проект и возвращает его.'''

        project = Project(**project_data)
        self.db.add(project)
        await self.db.commit()
        await self.db.refresh(project)
        return project
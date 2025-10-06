from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.db_depends import get_async_db
from app.models.projects import Project as ProjectModel
from app.schemas.projects_schemas import (
    ProjectCreate,
    Project as ProjectSchema
)


router = APIRouter(
    prefix='/projects',
    tags=['projects'],
)


@router.get('/', response_model=list[ProjectSchema])
async def get_all_projects(db: AsyncSession = Depends(get_async_db)):
    '''Возвращает список всех проектов.'''

    projects_query = await db.scalars(select(ProjectModel))
    return projects_query.all()


@router.get('/all', response_model=list[ProjectSchema])
async def get_is_active_projects(db: AsyncSession = Depends(get_async_db)):
    '''Возвращает список всех активных проектов.'''

    projects_query = await db.scalars(select(ProjectModel)
                                      .where(ProjectModel.is_active))
    return projects_query.all()


@router.get('/{project_id}',
            response_model=ProjectSchema,
            status_code=status.HTTP_200_OK)
async def get_project(project_id: int, db: AsyncSession = Depends(get_async_db)):
    '''Возвращает проект по его ID.'''
    pass


@router.post('/',
             response_model=ProjectSchema,
             status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate, db: AsyncSession = Depends(get_async_db)):
    '''Создает новый проект. ДОСТУПНО ТОЛЬКО АДМИНУ!'''
    pass


@router.put('/{project_id}',
            response_model=ProjectSchema,
            status_code=status.HTTP_200_OK)
async def update_project(project_id: int, db: AsyncSession = Depends(get_async_db)):
    '''Обновлет товар по его ID. ДОСТУПНО ТОЛЬКО АДМИНУ!'''
    pass


@router.delete('/{project_id}',
               response_model=ProjectSchema)
async def delete_project(project_id: int, db: AsyncSession = Depends(get_async_db)):
    '''Выполняет логическое удаление проекта. ДОСТУПНО ТОЛЬКО АДМИНУ!'''
    pass
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    status
)
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from your_dev.core.dependencies import get_admin_profile_service
from your_dev.data import PROJECTS_DATA

from your_dev.core import templates
from your_dev.core.database import get_async_db
from your_dev.services.users_services import AdminProfileService
# from your_dev.models.projects import Project as ProjectModel
# from your_dev.schemas.projects_schemas import (
#     ProjectCreate,
#     Project as ProjectSchema
# )


router = APIRouter(
    prefix='/projects',
    tags=['projects'],
)


@router.get('/{project_id}', response_class=HTMLResponse)
async def project_detail(
    request: Request,
    project_id: str,
    profile_service: AdminProfileService = Depends(get_admin_profile_service)
):
    project = PROJECTS_DATA.get(project_id)
    profile_data = await profile_service.get_active_profile()
    if not project:
        return templates.TemplateResponse('404.html', {'request': request})

    return templates.TemplateResponse('project.html', {
        'request': request,
        'project': project,
        'profile': profile_data
    })


# @router.get('/', response_model=list[ProjectSchema])
# async def get_all_projects(db: AsyncSession = Depends(get_async_db)):
#     '''Возвращает список всех проектов.'''

#     projects_query = await db.scalars(select(ProjectModel))
#     return projects_query.all()


# @router.get('/all', response_model=list[ProjectSchema])
# async def get_is_active_projects(db: AsyncSession = Depends(get_async_db)):
#     '''Возвращает список всех активных проектов.'''

#     projects_query = await db.scalars(select(ProjectModel)
#                                       .where(ProjectModel.is_active))
#     return projects_query.all()


# @router.get('/{project_id}',
#             response_model=ProjectSchema,
#             status_code=status.HTTP_200_OK)
# async def get_project(project_id: int, db: AsyncSession = Depends(get_async_db)):
#     '''Возвращает проект по его ID.'''
#     pass


# @router.post('/',
#              response_model=ProjectSchema,
#              status_code=status.HTTP_201_CREATED)
# async def create_project(project: ProjectCreate, db: AsyncSession = Depends(get_async_db)):
#     '''Создает новый проект. ДОСТУПНО ТОЛЬКО АДМИНУ!'''
#     pass


# @router.put('/{project_id}',
#             response_model=ProjectSchema,
#             status_code=status.HTTP_200_OK)
# async def update_project(project_id: int, db: AsyncSession = Depends(get_async_db)):
#     '''Обновлет товар по его ID. ДОСТУПНО ТОЛЬКО АДМИНУ!'''
#     pass


# @router.delete('/{project_id}',
#                response_model=ProjectSchema)
# async def delete_project(project_id: int, db: AsyncSession = Depends(get_async_db)):
#     '''Выполняет логическое удаление проекта. ДОСТУПНО ТОЛЬКО АДМИНУ!'''
#     pass
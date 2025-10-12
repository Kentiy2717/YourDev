from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    status
)
from fastapi.responses import HTMLResponse

from your_dev.core.dependencies import get_project_service

from your_dev.core import templates
from your_dev.services.project_services import ProjectService


router = APIRouter(
    prefix='/projects',
    tags=['projects'],
)


@router.get('/{name_project}', response_class=HTMLResponse)
async def project_detail(
    request: Request,
    name_project: str,
    project_service: ProjectService = Depends(get_project_service)
):
    project = await project_service.get_active_project_by_name_project(name_project)
    if not project:
        return templates.TemplateResponse('404.html', {'request': request})

    return templates.TemplateResponse('project.html', {
        'request': request,
        'project': project
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
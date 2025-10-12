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

from your_dev.core.dependencies import get_service_service
from your_dev.core import templates

from your_dev.services.service_services import ServiceService


router = APIRouter(
    prefix='/services',
    tags=['services'],
)


@router.get('/', response_class=HTMLResponse)
async def services(
    request: Request,
    service_service: ServiceService = Depends(get_service_service)
):

    service_data = await service_service.get_all_active_services()
    return templates.TemplateResponse('services.html', {
        'request': request,
        'services': service_data,
    })


# @router.get('/', response_model=list[ServiceSchema])
# async def get_all_services(db: AsyncSession = Depends(get_async_db)):
#     '''Возвращает список всех проектов.'''

#     services_query = await db.scalars(select(ServiceModel))
#     return services_query.all()


# @router.get('/all', response_model=list[ServiceSchema])
# async def get_is_active_services(db: AsyncSession = Depends(get_async_db)):
#     '''Возвращает список всех активных проектов.'''

#     services_query = await db.scalars(select(ServiceModel)
#                                       .where(ServiceModel.is_active))
#     return services_query.all()


# @router.get('/{service_id}',
#             response_model=ServiceSchema,
#             status_code=status.HTTP_200_OK)
# async def get_service(service_id: int, db: AsyncSession = Depends(get_async_db)):
#     '''Возвращает проект по его ID.'''
#     pass


# @router.post('/',
#              response_model=ServiceSchema,
#              status_code=status.HTTP_201_CREATED)
# async def create_service(service: ServiceCreate, db: AsyncSession = Depends(get_async_db)):
#     '''Создает новый проект. ДОСТУПНО ТОЛЬКО АДМИНУ!'''
#     pass


# @router.put('/{service_id}',
#             response_model=ServiceSchema,
#             status_code=status.HTTP_200_OK)
# async def update_service(service_id: int, db: AsyncSession = Depends(get_async_db)):
#     '''Обновлет проект по его ID. ДОСТУПНО ТОЛЬКО АДМИНУ!'''
#     pass


# @router.delete('/{service_id}',
#                response_model=ServiceSchema)
# async def delete_service(service_id: int, db: AsyncSession = Depends(get_async_db)):
#     '''Выполняет логическое удаление проекта. ДОСТУПНО ТОЛЬКО АДМИНУ!'''
#     pass
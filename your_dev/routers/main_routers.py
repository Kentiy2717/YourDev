from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    status
)
from fastapi.responses import HTMLResponse

from your_dev.core import templates
from your_dev.core.dependencies import (
    get_admin_profile_service,
    get_project_service,
    get_service_service
)

from your_dev.services.service_services import ServiceService
from your_dev.services.users_services import AdminProfileService
from your_dev.services.project_services import ProjectService


router = APIRouter(
    prefix='',
    tags=['main'],
)


@router.get('/', response_class=HTMLResponse)
async def home(
    request: Request,
    profile_service: AdminProfileService = Depends(get_admin_profile_service),
    project_service: ProjectService = Depends(get_project_service),
    service_service: ServiceService = Depends(get_service_service)
):

    '''Подготавливает данные для передачи на главную станицу админа.'''

    profile_data = await profile_service.get_active_profile()
    active_projects = await project_service.get_all_active_projects()
    service_data = await service_service.get_all_active_services()
    return templates.TemplateResponse('main/index.html', {
        'request': request,
        'profile': profile_data,
        'projects': active_projects,
        'services': service_data
    })


# ПОКА НЕ ИСПОЛЬЗУЕТСЯ. ДЛЯ АДМИНКИ ПОТОМ БУДЕТ НУЖНА.
# @router.get('/get', response_model=list[UserSchema])
# async def get_users(db: AsyncSession = Depends(get_async_db)):
#     '''Возвращает всех активных заказчиков.'''

#     customer_query = await db.scalars(select(UserModel).where(
#         UserModel.role == 'customer',
#         UserModel.is_active
#     ))
#     return customer_query.all()


# @router.post('/',
#              response_model=UserSchema,
#              status_code=status.HTTP_201_CREATED)
# async def create_user(user: UserCreate,
#                       db: AsyncSession = Depends(get_async_db)):
#     '''Регистрирует нового заказчика.'''

#     user_db = await db.scalar(select(UserModel)
#                               .where(UserModel.email == user.email))
#     if user_db:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT,
#                             detail='Email already registered')

#     db_user = UserModel(
#         email=user.email,
#         hashed_password=hash_password(user.password),
#     )

#     db.add(db_user)
#     await db.commit()
#     await db.refresh(db_user)
#     return db_user


# @router.post('/create_admin',
#              response_model=UserSchema,
#              status_code=status.HTTP_201_CREATED)
# async def create_admin(user: AdminCreate,
#                        db: AsyncSession = Depends(get_async_db)):
#     '''Регистрирует админа (работает только один раз).
#     Не может быть двух владельцев сайта.'''

#     admin = await db.scalar(select(UserModel).where(UserModel.role == 'admin'))
#     if admin:
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail='Невозможно зарегистрировать еще одного владельца сайта'
#         )

#     db_admin = UserModel(
#         email=user.email,
#         hashed_password=hash_password(user.password),
#         role='admin'
#     )

#     db.add(db_admin)
#     await db.commit()
#     await db.refresh(db_admin)
#     return db_admin
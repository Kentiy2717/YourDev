from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    status
)
from fastapi.responses import HTMLResponse

from your_dev.core import templates
from your_dev.core.dependencies import get_admin_profile_service
from your_dev.models.users import User as UserModel
from your_dev.schemas.users_schemas import (
    AdminProfileCreate,
    User as UserSchema,
    UserCreate
)

from your_dev.data import PROJECTS_DATA, SERVICES_DATA
from your_dev.services.users_services import AdminProfileService


router = APIRouter(
    prefix='',
    tags=['main'],
)


@router.get('/', response_class=HTMLResponse)
async def home(
    request: Request,
    profile_service: AdminProfileService = Depends(get_admin_profile_service)
):

    '''Подготавливает данные для передачи на главную станицу админа.'''

    profile_data = await profile_service.get_active_profile()
    return templates.TemplateResponse('index.html', {
        'request': request,
        'profile': profile_data,
        'projects': PROJECTS_DATA,
        'services': SERVICES_DATA
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
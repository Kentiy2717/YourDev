from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import hash_password
from app.dependencies.db_depends import get_async_db
from app.models.users import User as UserModel
from app.schemas.users_schemas import (
    AdminCreate,
    User as UserSchema,
    UserCreate
)


router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get('/get', response_model=list[UserSchema])
async def get_users(db: AsyncSession = Depends(get_async_db)):
    '''Возвращает всех активных заказчиков.'''

    customer_query = await db.scalars(select(UserModel).where(
        ~UserModel.is_admin,
        UserModel.is_active
    ))
    return customer_query.all()


@router.post('/',
             response_model=UserSchema,
             status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate,
                      db: AsyncSession = Depends(get_async_db)):
    '''Регистрирует нового заказчика.'''

    user_db = await db.scalar(select(UserModel)
                              .where(UserModel.email == user.email))
    if user_db:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='Email already registered')

    db_user = UserModel(
        email=user.email,
        hashed_password=hash_password(user.password),
    )

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


@router.post('/create_admin',
             response_model=UserSchema,
             status_code=status.HTTP_201_CREATED)
async def create_admin(user: AdminCreate,
                       db: AsyncSession = Depends(get_async_db)):
    '''Регистрирует админа (работает только один раз).
    Не может быть двух владельцев сайта.'''

    admin = await db.scalar(select(UserModel).where(UserModel.is_admin))
    if admin:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Невозможно зарегистрировать еще одного владельца сайта'
        )

    db_admin = UserModel(
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(db_admin)
    await db.commit()
    await db.refresh(db_admin)
    return db_admin
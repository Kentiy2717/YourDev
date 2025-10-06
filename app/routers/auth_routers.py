import jwt

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordRequestForm

from app.auth import (
    create_access_token,
    create_refresh_token,
    verify_password
)
from app.config import SECRET_KEY, ALGORITHM
from app.dependencies.db_depends import get_async_db
from app.models.users import User as UserModel


router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db: AsyncSession = Depends(get_async_db)):
    '''Аутентифицирует пользователя и возвращает
    access_token и refresh_token.'''

    user = await db.scalar(select(UserModel)
                           .where(UserModel.email == form_data.username))

    if not user or not verify_password(form_data.password,
                                       user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )
    access_token = create_access_token(data={
        'sub': user.email,
        'is_admin': user.is_admin,
        'id': user.id
    })
    refresh_token = create_refresh_token(data={
        'sub': user.email,
        'is_admin': user.is_admin,
        'id': user.id
    })
    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'token_type': 'bearer'
    }


@router.post('/refresh-token')
async def refresh_token(refresh_token: str,
                        db: AsyncSession = Depends(get_async_db)):
    '''Обновляет access_token с помощью refresh_token.'''

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate refresh token',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception

    user = await db.scalar(select(UserModel)
                           .where(UserModel.email == email,
                                  UserModel.is_active))
    if user is None:
        raise credentials_exception

    access_token = create_access_token(data={
        'sub': user.email,
        'is_admin': user.is_admin,
        'id': user.id
    })
    return {'access_token': access_token, 'token_type': 'bearer'}

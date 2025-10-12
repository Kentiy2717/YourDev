from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
import jwt
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from your_dev.core.config import settings
from your_dev.core.database import get_async_db
from your_dev.models.users import User as UserModel


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='users/token')


def hash_password(password: str) -> str:
    '''Преобразует пароль в хеш с использованием bcrypt.'''

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    '''Проверяет, соответствует ли введённый пароль сохранённому хешу.'''

    return pwd_context.verify(plain_password, hashed_password)


# def create_access_token(data: dict):
#     '''Создаёт JWT с payload (sub, role, id, exp).'''

#     to_encode = data.copy()
#     expire = datetime.now(timezone.utc) + timedelta(
#         minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
#     )
#     to_encode.update({'exp': expire})
#     return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


# def create_refresh_token(data: dict):
#     '''Создаёт рефреш-токен с длительным сроком действия.'''

#     to_encode = data.copy()
#     expire = datetime.now(timezone.utc) + timedelta(
#         days=settings.REFRESH_TOKEN_EXPIRE_DAYS
#     )
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


# async def get_current_user(token: str = Depends(oauth2_scheme),
#                            db: AsyncSession = Depends(get_async_db)):
#     '''Проверяет JWT и возвращает пользователя из базы. '''

#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail='Could not validate credentials',
#         headers={'WWW-Authenticate': 'Bearer'},
#     )
#     try:
#         payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
#         email: str = payload.get('sub')
#         if email is None:
#             raise credentials_exception
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail='Token has expired',
#             headers={'WWW-Authenticate': 'Bearer'},
#         )
#     except jwt.PyJWTError:
#         raise credentials_exception
#     user = await db.scalar(select(UserModel).where(UserModel.email == email,
#                                                    UserModel.is_active))
#     if user is None:
#         raise credentials_exception
#     return user


# async def get_current_seller(
#         current_user: UserModel = Depends(get_current_user)
# ) -> HTTPException | UserModel:
#     '''Проверяет, что пользователь является adminom.'''
#     if not current_user.is_admin:
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#                             detail='Only sellers can perform this action')
#     return current_user

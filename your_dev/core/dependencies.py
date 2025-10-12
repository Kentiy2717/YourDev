'''Прочие зависимости'''
from typing import TYPE_CHECKING
from fastapi import Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession

from your_dev.repositories.projects_repository import ProjectRepository
from your_dev.repositories.users_repository import (
    AdminProfileRepository,
    UserRepository
)
from your_dev.core.database import get_async_db
from your_dev.services.users_services import AdminProfileService
from your_dev.services.project_services import ProjectService

if TYPE_CHECKING:
    from your_dev.repositories.users_repository import (
        AdminProfileRepository,
        UserRepository
    )
    from your_dev.schemas.users_schemas import (
        AdminProfile,
        AdminProfileCreate,
        User,
        UserCreate
    )


# РЕПОЗИТОРИИ
def get_user_repository(
        db: AsyncSession = Depends(get_async_db)) -> UserRepository:
    return UserRepository(db)


def get_admin_profile_repository(
        db: AsyncSession = Depends(get_async_db)) -> AdminProfileRepository:
    return AdminProfileRepository(db)


def get_project_repository(
        db: AsyncSession = Depends(get_async_db)) -> ProjectRepository:
    return ProjectRepository(db)


# СЕРВИСЫ
def get_admin_profile_service(
    user_repo: UserRepository = Depends(get_user_repository),
    profile_repo: AdminProfileRepository = Depends(get_admin_profile_repository)
) -> AdminProfileService:
    return AdminProfileService(user_repo, profile_repo)


def get_project_service(
        project_repo: UserRepository = Depends(get_project_repository)
) -> ProjectService:
    return ProjectService(project_repo)


# def check_user_is_admin(current_user: User = Depends(get_current_user)) -> User:
#     '''Зависимость, которая возвращает ТОЛЬКО админов'''

#     if current_user.role != 'admin':
#         raise HTTPException(
#             status_code=403,
#             detail='У вас недостаточно прав доступа, чтобы просматривать эту страницу'
#         )
#     return current_user


# def check_user_is_admin(current_user: User = Depends(get_current_user)) -> User:
#     '''Зависимость, которая возвращает ТОЛЬКО админов'''

#     if current_user.role != 'admin':
#         raise HTTPException(
#             status_code=403,
#             detail='У вас недостаточно прав доступа, чтобы просматривать эту страницу'
#         )
#     return current_user


# Для JWT токенов
# from fastapi.security import HTTPBearer

# security = HTTPBearer()

# async def get_current_user(
#     credentials: HTTPAuthorizationCredentials = Depends(security),
#     db: AsyncSession = Depends(get_async_db)
# ) -> User:
#     '''Получаем текущего пользователя из JWT токена'''
#     token = credentials.credentials
    
#     try:
#         # Декодируем JWT токен
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id = payload.get('user_id')
        
#         if not user_id:
#             raise HTTPException(status_code=401, detail='Invalid token')
        
#         # Получаем пользователя из базы
#         user = await db.get(User, int(user_id))
#         if not user or not user.is_active:
#             raise HTTPException(status_code=401, detail='User not found or inactive')
        
#         return user
        
#     except jwt.JWTError:
#         raise HTTPException(status_code=401, detail='Invalid token')




# dependencies.py

# # Для строгих админских действий
# def get_current_admin(current_user: User = Depends(get_current_user)) -> User:
#     if current_user.role != 'admin':
#         raise HTTPException(403, 'Admin access required')
#     return current_user

# # Для действий, которые могут делать админы И владельцы
# def get_admin_or_owner(
#     resource_owner_id: int,
#     current_user: User = Depends(get_current_user)
# ) -> User:
#     if current_user.role != 'admin' and current_user.id != resource_owner_id:
#         raise HTTPException(403, 'Access denied')
#     return current_user

# # Для проверки конкретных разрешений
# def require_permission(permission: str):
#     def dependency(current_user: User = Depends(get_current_user)) -> User:
#         if not current_user.has_permission(permission):
#             raise HTTPException(403, f'Permission {permission} required')
#         return current_user
#     return dependency
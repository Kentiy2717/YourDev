from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.ext.asyncio import AsyncSession

from your_dev.models.users import User
from your_dev.repositories.projects_repository import ProjectRepository
from your_dev.repositories.service_repository import ServiceRepository
from your_dev.repositories.users_repository import (
    AdminProfileRepository,
    UserRepository
)
from your_dev.core.database import get_async_db
from your_dev.services.service_services import ServiceService
from your_dev.services.users_services import AdminProfileService, UserService
from your_dev.services.project_services import ProjectService


# РЕПОЗИТОРИИ
async def get_user_repository(
        db: AsyncSession = Depends(get_async_db)) -> UserRepository:
    return UserRepository(db)


async def get_admin_profile_repository(
        db: AsyncSession = Depends(get_async_db)) -> AdminProfileRepository:
    return AdminProfileRepository(db)


async def get_project_repository(
        db: AsyncSession = Depends(get_async_db)) -> ProjectRepository:
    return ProjectRepository(db)


async def get_service_repository(
        db: AsyncSession = Depends(get_async_db)) -> ServiceRepository:
    return ServiceRepository(db)


# СЕРВИСЫ
async def get_admin_profile_service(
    user_repo: UserRepository = Depends(get_user_repository),
    profile_repo: AdminProfileRepository = Depends(get_admin_profile_repository)
) -> AdminProfileService:
    return AdminProfileService(user_repo, profile_repo)


async def get_user_service(
    user_repo: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(user_repo)


async def get_project_service(
        project_repo: ProjectRepository = Depends(get_project_repository)
) -> ProjectService:
    return ProjectService(project_repo)


async def get_service_service(
        service_repo: ServiceRepository = Depends(get_service_repository)
) -> ServiceService:
    return ServiceService(service_repo)


# Зависимость для получения текущего пользователя из сессии
async def get_current_user(
    request: Request,
    user_service: UserService = Depends(get_user_service)
) -> User:
    '''Получает текущего пользователя из сессии'''

    user_id = request.session.get('user_id')
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Не авторизован'
        )

    user = await user_service.get_user_by_id(user_id)
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Пользователь деактивирован'
        )

    return user


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
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    status,
    Form
)
from fastapi.responses import HTMLResponse, RedirectResponse

from your_dev.core import templates
from your_dev.core.dependencies import (
    get_admin_profile_service,
    get_project_service,
    get_current_user,
    get_user_service
)
from your_dev.models.users import User
from your_dev.services.users_services import AdminProfileService
from your_dev.services.project_services import ProjectService
from your_dev.services.users_services import UserService

router = APIRouter(
    prefix='',
    tags=['auth'],
)


@router.get('/login', response_class=HTMLResponse)
async def login_page(request: Request):
    '''Страница входа'''

    # Если пользователь уже авторизован, редирект на главную
    if request.session.get('user_id'):
        return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)

    return templates.TemplateResponse('auth/login.html', {
        'request': request
    })


@router.post('/login')
async def login(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    user_service: UserService = Depends(get_user_service)
):
    '''Обработка формы входа'''

    user = await user_service.authenticate_user(email, password)

    if not user:
        return templates.TemplateResponse(
            "auth/login.html",
            {
                "request": request,
                "error": "Неверный email или пароль"
            },
            status_code=401
        )
    request.session['user_id'] = user.id
    return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)


@router.get('/register', response_class=HTMLResponse)
async def register_page(request: Request):
    '''Страница регистрации'''
    # Если пользователь уже авторизован, редирект на главную
    if request.session.get('user_id'):
        return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)

    return templates.TemplateResponse('auth/register.html', {
        'request': request
    })

@router.post('/register')
async def register(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(None),
    middle_name: str = Form(None),
    user_service: UserService = Depends(get_user_service)
):
    '''Обработка формы регистрации'''
    try:
        user_data = {
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
            'middle_name': middle_name
        }
        
        user = await user_service.register_user(user_data)
        
        # Автоматически логиним пользователя после регистрации
        request.session['user_id'] = user.id
        
        # Редирект на главную после успешной регистрации
        return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
        
    except HTTPException as e:
        # В случае ошибки возвращаем на страницу регистрации с сообщением об ошибке
        return templates.TemplateResponse('register.html', {
            'request': request,
            'error': e.detail
        })


@router.get('/logout')
async def logout(request: Request):
    '''Выход пользователя'''

    request.session.pop('user_id', None)
    return RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)


@router.get('/profile', response_class=HTMLResponse)
async def profile_page(
    request: Request,
    current_user: User = Depends(get_current_user)
):
    '''Страница профиля пользователя'''
    return templates.TemplateResponse('users/profile.html', {
        'request': request,
        'current_user': current_user
    })


@router.get('/orders', response_class=HTMLResponse)
async def orders(
    request: Request,
    current_user: User = Depends(get_current_user),
    profile_service: AdminProfileService = Depends(get_admin_profile_service),
    project_service: ProjectService = Depends(get_project_service)
):
    '''Заказы - доступен только аутентифицированным пользователям'''

    profile_data = await profile_service.get_active_profile()
    active_projects = await project_service.get_all_active_projects()

    return templates.TemplateResponse('users/orders.html', {
        'request': request,
        'profile': profile_data,
        'projects': active_projects,
        'current_user': current_user
    })



















# import jwt

# from fastapi import (
#     APIRouter,
#     Depends,
#     HTTPException,
#     status
# )
# from sqlalchemy import select
# from sqlalchemy.ext.asyncio import AsyncSession
# from fastapi.security import OAuth2PasswordRequestForm

# from your_dev.core.auth import (
#     create_access_token,
#     create_refresh_token,
#     verify_password
# )
# from your_dev.core.config import settings
# from your_dev.core.database import get_async_db
# from your_dev.models.users import User as UserModel


# router = APIRouter(
#     prefix='/auth',
#     tags=['auth'],
# )


# async def login(form_data: OAuth2PasswordRequestForm = Depends(),
#                 db: AsyncSession = Depends(get_async_db)):
#     '''Аутентифицирует пользователя и возвращает
#     access_token и refresh_token.'''

#     user = await db.scalar(select(UserModel)
#                            .where(UserModel.email == form_data.username))

#     if not user or not verify_password(form_data.password,
#                                        user.hashed_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail='Incorrect email or password',
#             headers={'WWW-Authenticate': 'Bearer'},
#         )
#     access_token = create_access_token(data={
#         'sub': user.email,
#         'role': user.role,
#         'id': user.id
#     })
#     refresh_token = create_refresh_token(data={
#         'sub': user.email,
#         'role': user.role,
#         'id': user.id
#     })
#     return {
#         'access_token': access_token,
#         'refresh_token': refresh_token,
#         'token_type': 'bearer'
#     }


# @router.post('/refresh-token')
# async def refresh_token(refresh_token: str,
#                         db: AsyncSession = Depends(get_async_db)):
#     '''Обновляет access_token с помощью refresh_token.'''

#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail='Could not validate refresh token',
#         headers={'WWW-Authenticate': 'Bearer'},
#     )
#     try:
#         payload = jwt.decode(refresh_token,
#                              settings.SECRET_KEY,
#                              algorithms=[settings.ALGORITHM])
#         email: str = payload.get('sub')
#         if email is None:
#             raise credentials_exception
#     except jwt.PyJWTError:
#         raise credentials_exception

#     user = await db.scalar(select(UserModel)
#                            .where(UserModel.email == email,
#                                   UserModel.is_active))
#     if user is None:
#         raise credentials_exception

#     access_token = create_access_token(data={
#         'sub': user.email,
#         'role': user.role,
#         'id': user.id
#     })
#     return {'access_token': access_token, 'token_type': 'bearer'}

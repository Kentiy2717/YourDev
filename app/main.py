from fastapi import FastAPI

from app.routers import (
    auth_routers,
    projects_routers,
    services_routers,
    users_routers
)

app = FastAPI(
    title='🌎 YOUR PYTHON DEV',
    description='Python Full-Stack Developer Portfolio',
    version='1.0.0'
)

app.include_router(auth_routers.router)
app.include_router(projects_routers.router)
app.include_router(services_routers.router)
app.include_router(users_routers.router)


@app.get('/')
async def root():
    '''Корневой маршрут, подтверждающий, что API работает.'''
    return {'message': 'Добро пожаловать в API сервиса YourDev!'}

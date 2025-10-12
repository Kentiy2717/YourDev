from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from your_dev.routers import (
    auth_routers,
    main_routers,
    projects_routers,
    services_routers
)

app = FastAPI(
    title='🌎 YOUR PYTHON DEV',
    description='Python Full-Stack Developer Portfolio',
    version='1.0.0'
)

app.mount('/static', StaticFiles(directory='your_dev/static'), name='static')

# app.include_router(auth_routers.router)
app.include_router(projects_routers.router)
app.include_router(services_routers.router)
app.include_router(main_routers.router)


@app.get('/')
async def root():
    '''Корневой маршрут, подтверждающий, что API работает.'''

    return {'message': 'Добро пожаловать в API сервиса YourDev!'}

from fastapi.templating import Jinja2Templates

from app.core.logger import setup_logging

templates = Jinja2Templates(directory='app/templates')

setup_logging()
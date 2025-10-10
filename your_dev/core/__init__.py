from fastapi.templating import Jinja2Templates

from your_dev.core.logger import setup_logging

templates = Jinja2Templates(directory='your_dev/templates')

setup_logging()
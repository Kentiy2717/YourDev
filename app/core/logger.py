import sys

from loguru import logger

from app.core.config import settings


def setup_logging():
    '''Настройка логирования для приложения'''

    logger.remove()
    console_format = (
        '<green>{time:YYYY-MM-DD HH:mm:ss}</green> | '
        '<level>{level: <8}</level> | '
        '<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | '
        '<level>{message}</level>'
    )

    file_format = (
        '{time:YYYY-MM-DD HH:mm:ss} | '
        '{level: <8} | '
        '{name}:{function}:{line} | '
        '{message}'
    )

    logger.add(
        sys.stderr,
        format=console_format,
        level=settings.LOG_LEVEL,
        colorize=True,
        backtrace=settings.DEBUG,
        diagnose=settings.DEBUG
    )

    logger.add(
        'logs/errors.log',
        format=file_format,
        level='ERROR',
        rotation='10 MB',
        retention='30 days',
        compression='zip',
        encoding='utf-8'
    )

    logger.add(
        'logs/app.log', 
        format=file_format,
        level='INFO',
        rotation='50 MB',
        retention='7 days',
        compression='zip',
        encoding='utf-8'
    )

    if settings.DEBUG:
        logger.add(
            'logs/debug.log',
            format=file_format,
            level='DEBUG',
            rotation='10 MB',
            retention='1 days'
        )

    logger.info('✅ Logging configured successfully')


app_logger = logger
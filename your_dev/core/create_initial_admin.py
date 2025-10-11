import os

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from your_dev.core.auth import hash_password
from your_dev.core.database import get_async_db
from your_dev.models.users import User, AdminProfile
from your_dev.core.logger import logger


INITIAL_PROFILE_DATA = {
    'name': 'ИННОКЕНТИЙ МОТРИЙ',
    'title': '🐍 PYTHON FULL-STACK DEVELOPER 🐍',
    'slogan': '💡 Превращаю идеи в работающие решения',
    'about': ('За 2 года погрузился в Python-разработку, прошел путь от '
              'пет-проектов до коммерческой разработки. Специализируюсь на '
              'создании web-приложений (бэкенд - FastAPI, Flask, '
              'Django, фронт на шаблонах), API и автоматизации. '
              'Верю в качественный код и постоянное обучение.'),
    'stats': {
        'опыт в IT': '2 года',
        'коммерческий опыт': '1 год',
        'завершенных проектов': '35+',
        'drunk coffee': '♾️',
    },
    'contacts': {
        'telegram': {'url': 'https://t.me/kentiy2717', 'text': '@kentiy2717', 'icon': 'fab fa-telegram'},
        'email': {'url': 'mailto:kentiy93@gmail.com', 'text': 'kentiy93@gmail.com', 'icon': 'fas fa-rocket'},
        'github': {'url': 'https://github.com/Kentiy2717', 'text': 'Kentiy2717', 'icon': 'fab fa-github'},
        'hh': {'url': '#', 'text': 'РЕЗЮМЕ', 'icon': 'fas fa-briefcase'}
    }
}


async def create_initial_admin():
    db: AsyncSession = get_async_db()
    try:
        # Проверяем, есть ли уже админ
        existing_admin = await db.scalar(select(User)
                                         .where(User.role == 'admin'))
        if existing_admin:
            logger.info('✅ Админ уже существует')
            return

        # Создаем админа
        admin_user = User(
            email=os.getenv('INITIAL_ADMIN_EMAIL'),
            first_name='Иннокентий',
            middle_name='Александрович',
            last_name='Мотрий',
            hashed_password=hash_password(os.getenv('INITIAL_ADMIN_PASSWORD')),
            role='admin'
        )
        db.add(admin_user)
        db.flush()  # Получаем ID

        # Создаем начальный профиль админа
        admin_profile = AdminProfile(
            user_id=admin_user.id,
            name_for_index=INITIAL_PROFILE_DATA['name'],
            title=INITIAL_PROFILE_DATA['title'],
            slogan=INITIAL_PROFILE_DATA['slogan'],
            about=INITIAL_PROFILE_DATA['about'],
            stats=INITIAL_PROFILE_DATA['stats'],
            contacts=INITIAL_PROFILE_DATA['contacts'],
        )

        db.add(admin_profile)
        await db.commit()
        logger.info('✅ Админ успешно создан')

    except Exception as e:
        logger.error(f'❌ Ошибка при создании админа: {e}')
        await db.rollback()

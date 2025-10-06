from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(
    title='🌎 YOUR PYTHON DEV',
    description='Elite Python Backend Developer Portfolio',
    version='2.0.0'
)

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

PROFILE_DATA = {
    'name': 'ИННОКЕНТИЙ МОТРИЙ',
    'title': '🐍 PYTHON FULL-STACK DEVELOPER 🐍',
    'tagline': '💡 Превращаю идеи в работающие решения',
    'about': ('За 2 года погрузился в Python-разработку, прошел путь от '
              'пет-проектов до коммерческой разработки. Специализируюсь на '
              'создании web-приложений (бэкенд - FastAPI, Flask, '
              'Django, фронт на шаблонах), API и автоматизации. '
              'Верю в качественный код и постоянное обучение.'),
    'stats': {
        'опыт в IT': '2 года',
        'коммерческий опыт': '1 год', 
        'завершенных проектов': '35+',
        'drunk coffee': '∞ чашек'
    },
    'contacts': {
        'telegram': {'url': 'https://t.me/kentiy2717', 'text': '@kentiy2717', 'icon': 'fab fa-telegram'},
        'email': {'url': 'mailto:kentiy93@gmail.com', 'text': 'kentiy93@gmail.com', 'icon': 'fas fa-rocket'},
        'github': {'url': 'https://github.com/Kentiy2717', 'text': 'Kentiy2717', 'icon': 'fab fa-github'},
        'hh': {'url': '#', 'text': 'РЕЗЮМЕ', 'icon': 'fas fa-briefcase'}
    }
}

PROJECTS_DATA = {
    'yacut': {
        'id': 'yacut',
        'title': '✂️ YACUT - СЕРВИС СОКРАЩЕНИЯ ССЫЛОК',
        'badge': 'УЧЕБНЫЙ',
        'description': 'Учебный проект для освоения Flask. Сокращает длинные ссылки и предоставляет API для интеграций.',
        'long_description': '**Учебный проект** разработанный в рамках изучения фреймворка **Flask**. Сервис преобразует длинные ссылки в короткие, а также позволяет производить **асинхронную загрузку** копий файлов на Яндекс.Диск с созданием короткой ссылки для их скачивания.',
        'highlights': [
            '🚀 Работа с Flask и ORM',
            '⚡ REST API разработка',
            '🛡️ База данных и миграции',
            '🎯 Простая и понятная архитектура'
        ],
        'technologies': ['Python', 'Flask', 'SQLite', 'REST API'],
        'github_url': 'https://github.com/Kentiy2717/yacut',
        'demo_url': '#',
        'status': 'Завершен',
        'complexity': 2,
        'automation_level': 70,
        'metrics': {
            'тип': 'Учебный проект',
            'статус': 'Завершен',
            'технологии': 'Flask, SQLAlchemy, SQLite',
            'цель': 'Изучение фреймворка Flask'
        }
    },
    'plc-system': {
        'id': 'plc-system', 
        'title': '🏭 СИСТЕМА ТЕСТИРОВАНИЯ ПЛК',
        'badge': 'INDUSTRY',
        'description': 'Система автоматизированного тестирования ПЛК с веб-интерфейсом',
        'long_description': 'Комплексное решение для автоматизации тестирования промышленных контроллеров. Включает веб-интерфейс, систему отчетности и интеграцию с промышленным оборудованием.',
        'highlights': [
            '🚀 Веб-интерфейс на Django',
            '⚡ Работа с PyModbus',
            '📻 Интеграция с оборудованием',
            '🎯 400+ автотестов'
        ],
        'technologies': ['Django', 'Python', 'PyModbus', 'Server-Sent Events', 'CI/CD'],
        'github_url': 'https://github.com/Kentiy2717/',
        'demo_url': '#',
        'status': 'Внедрен в производство',
        'complexity': 5,
        'automation_level': 95,
        'metrics': {
            'автотесты': '400+',
            'эффективность': '95%',
            'мониторинг': 'РЕАЛЬНОЕ ВРЕМЯ',
            'сбои': '0'
        }
    }
}

SERVICES_DATA = [
    {
        'title': '🔧 РАЗРАБОТКА ПОД КЛЮЧ',
        'description': 'Полный цикл: от идеи до работающего решения на хостинге. Бэкенд, фронт на шаблонах, деплой и базовая настройка.',
        'price': 'от 25K ₽',
        'features': [
            'Анализ требований и проектирование',
            'Backend на Python (FastAPI/Django/Flask)', 
            'Frontend на Jinja2 шаблонах',
            'Деплой на хостинг и настройка',
            'Базовая SEO оптимизация',
            'Техническая документация'
        ],
        'process': [
            {'step': '01', 'title': 'Обсуждение', 'desc': 'Погружаемся в задачу, определяем цели, погружаемся в предметную область'},
            {'step': '02', 'title': 'Прототип', 'desc': 'Выбираем необходимый стек. Создаем работающий прототип за 2-3 дня'},
            {'step': '03', 'title': 'Разработка', 'desc': 'Полноценная разработка с тестированием. Разработка визуальных шаблонов. Проработка бизнес-логики'},
            {'step': '04', 'title': 'Запуск', 'desc': 'Деплой на хостинг и обучение работе с системой. Передача документации и отчетности по проделанным работам'}
        ],
        'technologies': ['Python', 'FastAPI/Flask/Django', 'Jinja2', 'PostgreSQL', 'Docker'],
        'cta': 'Обсудить проект',
        'icon': 'fas fa-rocket',
        'highlight': True
    },
    {
        'title': '🔧 BACKEND DEVELOPMENT', 
        'description': 'Разрабатываю API и серверную логику. Интеграции с базами данных, внешними сервисами, аутентификация.',
        'price': 'от 15K ₽',
        'features': [
            'REST API разработка',
            'Работа с базами данных',
            'Интеграция сторонних API',
            'Аутентификация и авторизация',
            'Тестирование и документация'
        ],
        'technologies': ['Python', 'FastAPI/Flask/Django', 'SQLAlchemy'],
        'cta': 'Нужен бэкенд?',
        'icon': 'fas fa-server',
        'highlight': False
    },
    {
        'title': '🤖 АВТОМАТИЗАЦИЯ',
        'description': 'Пишу скрипты и ботов для автоматизации рутины. Парсинг, обработка данных, телеграм боты, Excel отчеты.',
        'price': 'от 10K ₽',
        'features': [
            'Парсинг сайтов и данных',
            'Телеграм боты',
            'Обработка Excel/CSV',
            'Автоматизация отчетности',
            'Интеграция с Google Sheets'
        ],
        'technologies': ['Python', 'aiohttp', 'BeautifulSoup', 'aiogram'],
        'cta': 'Автоматизировать',
        'icon': 'fas fa-robot',
        'highlight': False
    },
    {
        'title': '⚡ ДОРАБОТКА САЙТОВ',
        'description': 'Помогаю улучшить существующие проекты. Новый функционал, исправление ошибок, оптимизация.',
        'price': 'от 8K ₽',
        'features': [
            'Добавление нового функционала',
            'Исправление багов',
            'Оптимизация производительности',
            'Интеграция новых сервисов',
            'Техническая поддержка'
        ],
        'technologies': ['Python', 'FastAPI', 'Django', 'Flask'],
        'cta': 'Улучшить проект',
        'icon': 'fas fa-tools',
        'highlight': False
    },
]

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse('index.html', {
        'request': request,
        'profile': PROFILE_DATA,
        'projects': PROJECTS_DATA,
        'services': SERVICES_DATA
    })

@app.get('/projects/{project_id}', response_class=HTMLResponse)
async def project_detail(request: Request, project_id: str):
    project = PROJECTS_DATA.get(project_id)
    if not project:
        return templates.TemplateResponse('404.html', {'request': request})
    
    return templates.TemplateResponse('project.html', {
        'request': request,
        'project': project,
        'profile': PROFILE_DATA
    })

@app.get('/services', response_class=HTMLResponse)
async def services(request: Request):
    return templates.TemplateResponse('services.html', {
        'request': request,
        'services': SERVICES_DATA,
        'profile': PROFILE_DATA
    })

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
# 🌎 YourDev - Портфолио Full-Stack разработчика

[![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.118-green?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlalchemy&logoColor=white)](https://sqlalchemy.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue?logo=postgresql&logoColor=white)](https://postgresql.org)
[![JWT](https://img.shields.io/badge/JWT-Auth-orange?logo=jsonwebtokens&logoColor=white)](https://jwt.io/)

**Профессиональное портфолио** Full-Stack разработчика с современным дизайном и полным стеком технологий. Проект демонстрирует навыки в создании веб-приложений на Python, работе с базами данных и построении архитектуры приложений.

## 🎯 Особенности

- **🗄️ Полнофункциональное портфолио** с проектами и услугами
- **🎨 Стильный дизайн** с неоновыми эффектами и анимациями
- **🛠 Административная панель** для управления контентом
- **🔐 JWT аутентификация** с защищенными маршрутами
- **📱 Адаптивный дизайн** для всех устройств
- **⚡ Высокая производительность** благодаря асинхронному FastAPI
- **🔧 REST API** для интеграции с внешними сервисами

## 🏗️ Архитектура

Проект построен с использованием **многослойной архитектуры**, что обеспечивает:
- Четкое разделение ответственности между компонентами
- Легкую масштабируемость и поддержку кода
- Возможность тестирования отдельных модулей
- Гибкость в выборе и замене технологий

**Основные слои:**
- `models/` - SQLAlchemy модели данных
- `repositories/` - слой работы с базой данных (CRUD операции)
- `services/` - бизнес-логика приложения
- `schemas/` - Pydantic схемы для валидации данных
- `routes/` - API endpoints и веб-страницы
- `templates/` - Jinja2 шаблоны
- `static/` - статические файлы (CSS, JS, изображения)

## 🛠 Технологический стек

### Backend:
- **FastAPI 0.118** - современный асинхронный веб-фреймворк
- **SQLAlchemy 2.0** - ORM для работы с базой данных
- **Alembic 1.16** - миграции базы данных
- **Pydantic 2.11** - валидация данных и сериализация
- **JWT** - аутентификация и авторизация
- **bcrypt** - хеширование паролей

### База данных:
- **PostgreSQL** - основная реляционная база данных (через asyncpg)
- **SQLite** - для разработки и тестирования

### Фронтенд:
- **Jinja2** - шаблонизатор
- **HTML5/CSS3** - современная верстка с CSS Grid и Flexbox
- **JavaScript** - интерактивные элементы и анимации
- **Font Awesome** - иконки

### Безопасность:
- **JWT токены** - безопасная аутентификация
- **bcrypt** - защита паролей
- **CORS** - защита от межсайтовых запросов
- **Валидация данных** на уровне Pydantic схем

### Инфраструктура:
- **Uvicorn** - ASGI сервер
- **python-dotenv** - управление переменными окружения
- **Alembic** - управление миграциями базы данных

## 🐍 Быстрый старт

```bash
# Клонирование и установка
git clone https://github.com/Kentiy2717/YourDev.git
cd YourDev

# Виртуальное окружение
python -m venv venv
source venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac

# Зависимости
pip install -r requirements.txt

# Настройка окружения
cp .env.example .env
# Отредактируйте .env, указав:
# DATABASE_URL=postgresql+asyncpg://user:password@localhost/portfolio
# SECRET_KEY=your-secret-key
# ALGORITHM=HS256

# Настройка базы данных
alembic upgrade head

# Запуск приложения
py run.py
```
Приложение будет доступно по адресу: http://localhost:8000

# 📁 Структура проекта
```
portfolio/
├── app/
│   ├── models/           # SQLAlchemy модели
│   ├── repositories/     # Слой работы с БД
│   ├── services/         # Бизнес-логика
│   ├── schemas/          # Pydantic схемы
│   ├── routes/           # Маршруты и API endpoints
│   ├── templates/        # Jinja2 шаблоны
│   ├── static/           # Статические файлы
│   ├── auth.py           # Работа с JWT-токенами
│   ├── database.py       # Конфигурация БД
│   ├── config.py         # Настройки приложения
│   ├── main.py           # Точка входа
│   └── run.py            # Быстрый запуск приложения
├── migrations/           # Миграции Alembic
├── requirements.txt
└── README.md
```

## 👉 API Endpoints

### ✅ Публичные маршруты:
- **GET /** - главная страница портфолио
- **GET /services** - страница услуг
- **GET /projects/{project_id}** - детальная страница проекта
- **GET /api/v1/projects** - API списка проектов
- **GET /api/v1/services** - API списка услуг

### 🛡️ Защищенные маршруты (JWT):
- **POST /api/v1/auth/login** - аутентификация
- **POST /api/v1/auth/register** - регистрация
- **POST /api/v1/projects** - создание проекта (админ)
- **PUT /api/v1/projects/{id}** - обновление проекта (админ)
---
### 📈 Планы развития
- Административная панель для управления контентом
- Блог с техническими статьями
- Система комментариев к проектам
- Интеграция с GitHub API для автоматического обновления проектов
- Многоязычная поддержка
- PWA функциональность
- Docker контейнеризация
---
---
---
---
---
# 👨‍💻 Автор
Иннокентий Мотрий - Python Full-Stack Developer
---
- ☁️ GitHub: @Kentiy2717
- 📱 Telegram: @kentiy2717
- 📫 Email: kentiy93@gmail.com
- 🌐 Сайт: www.your-dev.ru (чуть позже)
---
📄 Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

# from your_dev.models.services import Service


class ServiceRepository:
    def __init__(self, db: AsyncSession):
        self.db = db
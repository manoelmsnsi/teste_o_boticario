import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

metadata = sqlalchemy.MetaData()

class Database:
    def __init__(self):
        DATABASE_URL = os.environ.get("DATABASE_URL", None)
        self.engine = create_async_engine(DATABASE_URL, echo=True, future=True)
        self.sessionmaker = sessionmaker(self.engine, class_=AsyncSession)

    @asynccontextmanager
    async def conexao(self):
        try:
            async with self.sessionmaker() as session:
                yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()

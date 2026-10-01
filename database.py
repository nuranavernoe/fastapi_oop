from .core.config import settings

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

async_engine = create_async_engine(
    url = settings.DATABASE_URL_asyncpg,
    echo=True
)

async_session_factory = async_sessionmaker(
    bind=async_engine,
    explire_on_commit=False
)


async def get_db():
    async with  async_session_factory() as session:
        yield session
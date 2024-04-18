from asyncio import current_task
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)
from core.settings import settings


class DBHelper:
    def __init__(self, url, echo):
        self.engine = create_async_engine(url=url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, expire_on_commit=False
        )

    async def sessionmaker_dependency(self):
        async with self.session_factory() as session:
            yield session
            session.close()

    def scoped_session(self):
        AsyncScopedSession = async_scoped_session(
            self.session_factory,
            scopefunc=current_task,
        )

        return AsyncScopedSession

    def scoped_session_dependency(self):
        scoped_async_session = self.scoped_session()
        yield scoped_async_session
        scoped_async_session.remove()


db_helper = DBHelper(settings.url, settings.echo)

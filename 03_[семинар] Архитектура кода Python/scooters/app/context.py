# vibo: в файле контекст сделаем подключение к папке с секретами и БД

# vibo: заведем типы
import typing as tp

# vibo: библиотека для работы с postgres
import asyncpg

# vibo: Не используем ORM Object-Relational Mapping (способ взаимодействовать с базой из кода)
# vibo: взяли самую простую библиотеку, клиент для работы с postrges asyncpg,
# vibo: чтбы работать с простыми sql-запрсоами

from app.utils import secrets

# vibo: импортируем модуль с геокодером
from app.utils import geocode

# vibo: создаем класс AppContext, у класса всего два метода
# vibo: т.к. мы планируем использовать внешнюю БД удобно сделать метод на ее открытие и закрытие
class AppContext:
    def __init__(self, *, secrets_dir: str):
        self.secrets: secrets.SecretsReader = secrets.SecretsReader(
            secrets_dir
        )
        self.db: tp.Optional[asyncpg.Pool] = None

        self.geocoder = geocode.GeocoderClient(
            self.secrets.get('ya_geocoder_api_key')
        )

    # vibo: первый метод класса - on_startup (запуск соединения с бд)
    async def on_startup(self, app=None):
        # vibo: передаем строчку подключения
        self.db = await asyncpg.create_pool(self.secrets.get('postgres_dsn'))

    # vibo: второй метод класса - on_shutdown (окончание соединения с бд)
    async def on_shutdown(self, app=None):
        if self.db:
            self.db.close()

# vibo: делаем функцию, которая будет доставать наши самокаты

# vibo: заведем типы
import typing as tp

# vibo: импортируем контекст
from app.context import AppContext

# vibo: импортируем модули
from app import models


'''
#vibo:
Есть такой антипатерн 'программирование на словарях' в питоне. Короче это плохо.
Хорошо - на объектах. Если говорим о конкретной функции, она должна возвращать список самокатов.
То, что связано с базой данных называется моделью
'''


async def get_scooters(context: AppContext) -> tp.List[models.Scooter]:
    # vibo: пишем код работы с базой данных
    sql = '''
    select id, location, user from scooters
    '''
    rows = await context.db.fetch(sql)

    # vibo: теперь строки из бд нужно перевести в объекты

    return [models.Scooter.from_db(row) for row in rows]

# vibo: объявляем метод

# vibo: импорт базы для нашего сервера
from aiohttp import web

# vibo: в качестве исключения импртируем в метод класс
from app.context import AppContext

# vibo: импортируем модуль
# from app import storage
from app.utils import scooters as scooters_utils
from app import dto

# vibo: обработчик будет принимать request, возвращать Response
async def handle(request: web.Request, context: AppContext) -> web.Response:
    # pass
    # vibo: забираем самокаты
    scooters = await scooters_utils.get_scooters(
        context, scooters_utils.GetScootersParams()
    )
    # vibo: протестируем работу
    # return web.json_response({'hello': 'test'})
    # vibo: возвращать нужно словарем, а не списком, чтобы потом проще было что-то добавить
    return web.json_response(
        {'items': [to_response(scooter) for scooter in scooters]}
    )


# vibo: функция, относящаяся к слою изображения, здесь словарь уже можно
def to_response(scooter: dto.Scooter) -> dict:
    return {
        'id': scooter.id,
        'location': [scooter.location.lat, scooter.location.lon],
    }

# vibo: объявляем метод

# vibo: импорт базы для нашего сервера
from aiohttp import web

# vibo: в качестве исключения импртируем в метод класс
from app.context import AppContext

# vibo: импортируем модули
from app.utils import scooters as scooters_utils
from app import dto


# vibo: обработчик будет принимать request, возвращать Response
async def handle(request: web.Request, context: AppContext) -> web.Response:

    # vibo: скопировали из get_scooters

    # pass
    # vibo: забираем самокаты
    scooters = await scooters_utils.get_scooters(
        context, scooters_utils.GetScootersParams(fetch_address=True)
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
        'location': {'lon': scooter.location.lon, 'lat': scooter.location.lat},
        # vibo: помним, что пользователь у нас может быть, а может не быть
        # vibo: делаем хак
        'user': scooter.user.id if scooter.user else None,
        'address': scooter.address,
    }


# vibo: трехслойная архитектура удобна тем, что на уровне storege мы используем одни и теже функции
# vibo: а на уровне отображения делаем что угодно, захотели в админке другой формат и сделали

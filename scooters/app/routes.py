from aiohttp import web

#vibo: импортируем созданные методы
from app.api.v1 import get_scooters
from app.api.v1 import get_scooters_admin

from app.context import AppContext

#vibo: декоратор @название - функция, возвращающая функцию
#vibo: в качестве аргументов принимаем ввод и контекст
def wrap_handler(handler, context):
    async def wrapper(request):
        return await handler(request, context)

    return wrapper

#vibo: ручка == handler, функция, которая вызывается в ответ на запрос какого-то url
#vibo: v1 - когда пишем продакт-сервис версионирование API критически важный момент

def setup_routes(app: web.Application, ctx: AppContext) -> None:
    app.router.add_get(
        '/v1/scooters', #vibo: ручка1 - /v1/scooters - обработчик для мобильного приложения
        wrap_handler(
            #vibo: добавляем метод
            get_scooters.handle,            
            ctx,
        ),
    )
    
    app.router.add_get(
        '/v1/admin/scooters', #vibo: ручка1 - /v1/admin/scooters - обработчик для админки
        wrap_handler(
            #vibo: добавляем метод
            get_scooters_admin.handle,  
            ctx,
        ),
    )

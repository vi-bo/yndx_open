# vibo: имеем шаблон
# vibo: запускаем python main.py --secrets-dir secret

import asyncio
import argparse

from aiohttp import web

from app.context import AppContext
from app import routes


async def create_app(args):
    # vibo: вызов Application, класс-приложение
    app = web.Application()
    # vibo: имплементируем контекст; для обработки запросов нам нужна внешняя база данных,
    # vibo: создаем класс AppContext, файл context,py в папке app
    ctx = AppContext(secrets_dir=args.secrets_dir)

    # vibo: два метода из класса AppContext (файл context.py в папке app)
    # vibo: т.к. мы планируем использовать внешнюю БД удобно сделать метод на ее открытие и закрытие
    app.on_startup.append(ctx.on_startup)
    app.on_shutdown.append(ctx.on_shutdown)

    # vibo: мы не хотим перечислять все хендлеры в функции main, хотм перенести их в отдельный модуль
    # vibo: отдельный модуль - routes.py, так же в папке app
    routes.setup_routes(app, ctx)

    return app


def parse_args():
    parser = argparse.ArgumentParser()
    # vibo: передаем не один аргумент, а папку с секретами
    parser.add_argument('--secrets-dir', type=str, required=True)

    return parser.parse_args()


# vibo: все начинается с функции main
def main():
    # vibo: функция main сразу парсит аргументы
    args = parse_args()
    # vibo: asyncio.get_event_loop().run_until_complete - чтобы запустить event_loop без ассинхронной функции
    # vibo: аргумент(имя папки) передается в функцию create_app
    app = asyncio.get_event_loop().run_until_complete(create_app(args))

    # vibo: метод из aiohttp, это фреймворк, построенный на базе asyncio для построения веб-приложений, веб-серверов
    web.run_app(app)


if __name__ == '__main__':
    main()

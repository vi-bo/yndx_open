from aiohttp import web
from aiohttp.web import run_app

async def handle(request):
    return web.Response(text='Meow.')

app = web.Application()
app.router.add_route('GET', '/', handle)
run_app(app, port=8888)
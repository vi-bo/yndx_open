from aiohttp import web
from aiohttp.web import run_app

async def test(request):
    print('Handler function called')
    return web.Response(text='Hello')

@web.middleware
async def middleware(request, handler):
    print('Middleware called')
    response = await handler(request)
    print('Middleware finished')
    return response

app = web.Application(middlewares=[middleware])
app.router.add_get('/', test)
web.run_app(app)
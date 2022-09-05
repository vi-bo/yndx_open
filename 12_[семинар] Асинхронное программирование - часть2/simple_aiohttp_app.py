import aiohttp
import asyncpg
from aiohttp import web
from aiohttp.web import run_app

async def init_pg(app):
    app['pg'] = await asyncpg.create_pool(
        #'postgresql://user:me@0.0.0.0/test'
        'postgresql://postgres:me@0.0.0.0/test'
    )

async def handle(request):
    async with request.app['pg'].acquire() as conn:
        row = await conn.fetchrow('SELECT 1 as col')
    return aiohttp.web.Response(body={'data': row})

app = web.Application()
app.router.add_route('GET', '/', handle)
app.on_startup.append(init_pg)
aiohttp.web.run_app(app, port=8082)
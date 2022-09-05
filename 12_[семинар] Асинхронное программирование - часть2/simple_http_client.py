import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://0.0.0.0:8888') as resp:
            print(resp.status) # body не можем распечатать - payloads
            print(await resp.text)

asyncio.run(main())
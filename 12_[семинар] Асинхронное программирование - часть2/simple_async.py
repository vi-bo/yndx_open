import asyncio
import time

async def get_text(delay, text):
    await asyncio.sleep(delay)
    return text

async def say_text():
    task1 = asyncio.create_task(get_text(5, 'hello'))
    task2 = asyncio.create_task(get_text(5, 'world'))
    await task1
    await task2
    return ', '.join([task1.result(), task2.result()])

result = asyncio.run(say_text())
print(result) # hello, world
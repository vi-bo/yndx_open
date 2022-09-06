import asyncio
import aiomisc
from aiomisc import entrypoint
from asyncio import AbstractEventLoop

async def main():
    loop = asyncio.get_event_loop()
    event = asyncio.Event()
    future = asyncio.Future()

    loop.call_soon(event.set)

    results = await aiomisc.select(future, event.wait())
    future_result, event_result = results

    print(results.result())                 # True
    print(results.result_idx)               # 0
    print(event_result, future_result)      # True, None

with aiomisc.entrypoint() as loop:
    loop.run_until_complete(main())
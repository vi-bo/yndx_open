import asyncio
import os
from aiomisc import entrypoint
from aiomisc.service import Profiler
import time

async def main():
    for i in range(100):
        time.sleep(0.01)

with entrypoint(Profiler(interval=0.1, top_results=5)) as loop:
    loop.run_until_complete(main())
#!/usr/bin/python3.7
import asyncio
import re
while True:
    break




async def f(n):
    await asyncio.sleep(n)
    with open("test","w") as f:
        f.write(str(n))
        f.close

async def asdf(n):
    asyncio.sleep(n)
    with open("test","w") as f:
        f.write(n)
        f.close



async def fuck():
    await f(20)
    await f(1)




asyncio.run(fuck())

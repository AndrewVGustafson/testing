import asyncio
import httpx
import time
import requests


async def async_fetch(amount):
    URL = "https://zenquotes.io/api/random"
    async with httpx.AsyncClient() as client:
        rs = [client.get(URL) for _ in range(amount)]
        results = await asyncio.gather(*rs)
    
    print([result.content for result in results])

def fetch(amount):
    URL = "https://zenquotes.io/api/random"
    
    rs = [requests.get(URL) for _ in range(amount)]
    print([r.content for r in rs])


def main():
    # start = time.perf_counter()
    # asyncio.run(async_fetch(3))
    # print(f"Asyncronous Time: {time.perf_counter() - start}")

    start = time.perf_counter()
    fetch(3)
    print(f"Sequential Time: {time.perf_counter() - start}")

if __name__ == "__main__":
    main()
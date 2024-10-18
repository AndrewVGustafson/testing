import trio # async library that selenium uses
from selenium import webdriver
import selenium.webdriver.common.devtools.v127 as cdp
from selenium.webdriver.remote.bidi_connection import BidiConnection

# cdp.

async def start_listening(listener):
    async for event in listener:
        # print(event.loader_id)
        pass


async def main():
    driver = webdriver.Chrome()

    async with driver.bidi_connection() as connection:
        session: BidiConnection = connection.session
        devtools: cdp = connection.devtools
        
        # await session.execute(devtools.fetch.enable())
        await session.execute(devtools.network.enable())

        # listener = session.listen(devtools.fetch.RequestPaused)
        listener = session.listen(devtools.network.ResponseReceived)
        async with trio.open_nursery() as nursery:
            nursery.start_soon(start_listening, listener) # start_listening blocks, so we run it in another coroutine

            driver.get('https://speedle.rahuljk.com/')


trio.run(main)
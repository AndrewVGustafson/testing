import requests
from PIL import Image
import asyncio
from timeit import default_timer

ASPECT_RATIO = 256
URL = "https://thispersondoesnotexist.com/"

def timed(func):
    def wrapper(*args):
        start_time = default_timer()
        func(*args)
        print(f"Time {func.__name__}(): {default_timer() - start_time}")
    return wrapper
    

@timed
def get_images_async(amount):

    async def func():
        loop = asyncio.get_event_loop()
        for i in range(amount):
            r = await loop.run_in_executor(None, requests.get, URL)
            filename = f"faces/{i}.jpg"

            with open(filename, "w+b") as f:
                f.write(r.content)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(func())

@timed
def get_images(amount):
    for i in range(amount):
        r = requests.get(URL)
        filename = f"faces/{i}.jpg"

        with open(filename, "w+b") as f:
            f.write(r.content)

@timed
def merge_images(amount):
    combined_img = Image.new("RGB", (ASPECT_RATIO, ASPECT_RATIO * (amount)), "white")
    for i in range(amount):
        filename = f'faces/{i}.jpg'
        img = Image.open(filename)

        img.thumbnail((ASPECT_RATIO, ASPECT_RATIO))
        img.save(filename)
        combined_img.paste(img, (0, ASPECT_RATIO * (i)))

    combined_img.show()

        

def main():
    amount = 3
    # get_images_async(amount)
    get_images(amount)
    merge_images(amount)

if __name__ == "__main__":
    main()
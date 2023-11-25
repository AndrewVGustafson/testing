import requests
from PIL import Image
from timeit import default_timer
from io import BytesIO
import numpy as np

ASPECT_RATIO = 256
URL = "https://thispersondoesnotexist.com/"

def timed(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        func(*args, **kwargs)
        print(f"Time {func.__name__}(): {default_timer() - start_time}")
    return wrapper
    
def fetch_image():
        r = requests.get(URL)
        return Image.open(BytesIO(r.content))

def is_square(x):
    return float(x**0.5).is_integer()

@timed
def merge_images(amount):
    layout =[]
    # np

    combined_img = Image.new("RGB", (ASPECT_RATIO, ASPECT_RATIO * (amount)), "white")
    for i in range(amount):
        img = fetch_image()
        img.thumbnail((ASPECT_RATIO, ASPECT_RATIO))
        combined_img.paste(img, (0, ASPECT_RATIO * (i)))

    combined_img.show()  

def main():
    merge_images(3)

if __name__ == "__main__":
    main()
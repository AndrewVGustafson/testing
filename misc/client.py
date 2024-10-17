import requests
from PIL import Image

def images(amount):
    for i in range(amount):
        r = requests.get("https://thispersondoesnotexist.com/")
        filename = i
        with open(f"{filename}.jpg", "w+b") as f:
            f.write(r.content)

        img = Image.open(f'{filename}.jpg')
        
        
        print(img.size)

def main():
    images(1)
    


if __name__ == "__main__":
    main()
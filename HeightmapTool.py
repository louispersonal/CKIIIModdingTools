import math

from PIL import Image

if __name__ == '__main__':
    img = Image.open("extras/heightmap.png")
    img = img.convert('RGB')
    pixels = list(img.getdata())

    out_img = Image.new('RGB', img.size)

    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            if 0 < pixel[0] < 14:
                out_img.putpixel((x, y), (0, 0, 0))
            if 13 < pixel[0] < 31:
                out_img.putpixel((x, y), (50, 50, 50))
            if 30 < pixel[0] < 51:
                out_img.putpixel((x, y), (100, 100, 100))
            if 50 < pixel[0] < 256:
                out_img.putpixel((x, y), (200, 200, 200))

    out_img.save('extras/heightmapSimplified.png')

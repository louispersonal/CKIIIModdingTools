import math

from PIL import Image

if __name__ == '__main__':
    img = Image.open("australia_size_adjusted.png")
    pixels = list(img.getdata())
    # list of tuples of 3 ints (RGB)

    forest_jungle = (11, 31, 4)
    forest_leaf = (8, 15, 7)
    sea = (11, 10, 50)
    drylands_grassy = (148, 125, 84)
    drylands = (152, 102, 65)
    desert_wavy = (255, 226, 167)
    plains = (55, 92, 25)
    desert_flat = (202, 118, 81)
    # mountains_desert = (94, 72, 48)
    approved_colors = [forest_jungle, forest_leaf, sea, drylands_grassy, drylands, desert_wavy, plains, desert_flat]

    out_forest_jungle = Image.new('RGB', img.size)
    out_forest_leaf = Image.new('RGB', img.size)
    out_sea = Image.new('RGB', img.size)
    out_drylands_grassy = Image.new('RGB', img.size)
    out_drylands = Image.new('RGB', img.size)
    out_desert_wavy = Image.new('RGB', img.size)
    out_plains = Image.new('RGB', img.size)
    out_desert_flat = Image.new('RGB', img.size)
    out_mountains_desert = Image.new('RGB', img.size)

    width, height = img.size

    for x in range(width):
        for y in range(height):
            closest_distance = 500  # this is greater than the difference between white and black
            new_color = approved_colors[0]  # set to random color, will get assigned later
            pixel = img.getpixel((x, y))
            for color in approved_colors:
                new_distance = math.dist(pixel, color)
                if new_distance < closest_distance:
                    closest_distance = new_distance
                    new_color = color
            if new_color == forest_jungle:
                out_forest_jungle.putpixel((x, y), (255, 255, 255))
            if new_color == forest_leaf:
                out_forest_leaf.putpixel((x, y), (255, 255, 255))
            if new_color == sea:
                out_sea.putpixel((x, y), (255, 255, 255))
            if new_color == drylands_grassy:
                out_drylands_grassy.putpixel((x, y), (255, 255, 255))
            if new_color == drylands:
                out_drylands.putpixel((x, y), (255, 255, 255))
            if new_color == desert_wavy:
                out_desert_wavy.putpixel((x, y), (255, 255, 255))
            if new_color == plains:
                out_plains.putpixel((x, y), (255, 255, 255))
            if new_color == desert_flat:
                out_desert_flat.putpixel((x, y), (255, 255, 255))
            # if new_color == mountains_desert:
                # out_mountains_desert.putpixel((x, y), (255, 255, 255))

    out_forest_jungle.save('forest_jungle_01_mask.png')
    out_forest_leaf.save('forest_leaf_01_mask.png')
    out_sea.save('beach_02_mask.png')
    out_drylands_grassy.save('drylands_01_grassy_mask.png')
    out_drylands.save('drylands_01_mask.png')
    out_desert_wavy.save('desert_wavy_01_mask.png')
    out_plains.save('plains_01_mask.png')
    out_desert_flat.save('desert_flat_01_mask.png')
    out_mountains_desert.save('mountain_02_desert_mask.png')

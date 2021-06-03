import math

from PIL import Image, ImageFilter


def satellite():
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


def climate_zones():
    img = Image.open("climatesAndTextures.png")
    pixels = list(img.getdata())
    # list of tuples of 3 ints (RGB)

    drylands_1_grassy_a = (173, 126, 4)
    forest_jungle_1 = (43, 67, 29)
    medi_grass_1 = (117, 160, 32)
    drylands_1_grassy_b = (180, 200, 84)
    medi_lumpy_grass = (211, 237, 161)
    drylands_1_cracked = (154, 0, 0)
    desert_cracked = (252, 133, 65)
    steppe_grass = (254, 232, 123)
    steppe_bushes = (222, 187, 7)
    medi_dry_mud = (246, 242, 194)
    medi_noisy_grass = (246, 248, 227)
    plains_01_noisy = (230, 191, 209)
    plains_01_rough = (69, 39, 101)
    hills_01 = (115, 204, 218)
    plains_01_dry = (130, 27, 116)
    black = (0, 0, 0)

    approved_colors = [drylands_1_grassy_a, forest_jungle_1, medi_grass_1, drylands_1_grassy_b, medi_lumpy_grass,
                       drylands_1_cracked, desert_cracked, steppe_grass, steppe_bushes, medi_dry_mud, medi_noisy_grass,
                       plains_01_noisy, plains_01_rough, hills_01, plains_01_dry, black]

    out_drylands_1_grassy = Image.new('RGB', img.size)
    out_forest_jungle_1 = Image.new('RGB', img.size)
    out_medi_grass_1 = Image.new('RGB', img.size)
    out_medi_lumpy_grass = Image.new('RGB', img.size)
    out_drylands_1_cracked = Image.new('RGB', img.size)
    out_desert_cracked = Image.new('RGB', img.size)
    out_steppe_grass = Image.new('RGB', img.size)
    out_steppe_bushes = Image.new('RGB', img.size)
    out_medi_dry_mud = Image.new('RGB', img.size)
    out_medi_noisy_grass = Image.new('RGB', img.size)
    out_plains_01_noisy = Image.new('RGB', img.size)
    out_plains_01_rough = Image.new('RGB', img.size)
    out_hills_01 = Image.new('RGB', img.size)
    out_plains_01_dry = Image.new('RGB', img.size)
    out_beach = Image.new('RGB', img.size)

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
            if new_color == drylands_1_grassy_a:
                out_drylands_1_grassy.putpixel((x, y), (255, 255, 255))
            if new_color == forest_jungle_1:
                out_forest_jungle_1.putpixel((x, y), (255, 255, 255))
            if new_color == medi_grass_1:
                out_medi_grass_1.putpixel((x, y), (255, 255, 255))
            if new_color == drylands_1_grassy_b:
                out_drylands_1_grassy.putpixel((x, y), (255, 255, 255))
            if new_color == medi_lumpy_grass:
                out_medi_lumpy_grass.putpixel((x, y), (255, 255, 255))
            if new_color == drylands_1_cracked:
                out_drylands_1_cracked.putpixel((x, y), (255, 255, 255))
            if new_color == desert_cracked:
                out_desert_cracked.putpixel((x, y), (255, 255, 255))
            if new_color == steppe_grass:
                out_steppe_grass.putpixel((x, y), (255, 255, 255))
            if new_color == steppe_bushes:
                out_steppe_bushes.putpixel((x, y), (255, 255, 255))
            if new_color == medi_dry_mud:
                out_medi_dry_mud.putpixel((x, y), (255, 255, 255))
            if new_color == medi_noisy_grass:
                out_medi_noisy_grass.putpixel((x, y), (255, 255, 255))
            if new_color == plains_01_noisy:
                out_plains_01_noisy.putpixel((x, y), (255, 255, 255))
            if new_color == plains_01_rough:
                out_plains_01_rough.putpixel((x, y), (255, 255, 255))
            if new_color == hills_01:
                out_hills_01.putpixel((x, y), (255, 255, 255))
            if new_color == plains_01_dry:
                out_plains_01_dry.putpixel((x, y), (255, 255, 255))
            if new_color == black:
                out_beach.putpixel((x, y), (255, 255, 255))

    blur_amount = 10

    out_drylands_1_grassy = out_drylands_1_grassy.filter(ImageFilter.BoxBlur(blur_amount))
    out_forest_jungle_1 = out_forest_jungle_1.filter(ImageFilter.BoxBlur(blur_amount))
    out_medi_grass_1 = out_medi_grass_1.filter(ImageFilter.BoxBlur(blur_amount))
    out_medi_lumpy_grass = out_medi_lumpy_grass.filter(ImageFilter.BoxBlur(blur_amount))
    out_drylands_1_cracked = out_drylands_1_cracked.filter(ImageFilter.BoxBlur(blur_amount))
    out_desert_cracked = out_desert_cracked.filter(ImageFilter.BoxBlur(blur_amount))
    out_steppe_grass = out_steppe_grass.filter(ImageFilter.BoxBlur(blur_amount))
    out_steppe_bushes = out_steppe_bushes.filter(ImageFilter.BoxBlur(blur_amount))
    out_medi_dry_mud = out_medi_dry_mud.filter(ImageFilter.BoxBlur(blur_amount))
    out_medi_noisy_grass = out_medi_noisy_grass.filter(ImageFilter.BoxBlur(blur_amount))
    out_plains_01_noisy = out_plains_01_noisy.filter(ImageFilter.BoxBlur(blur_amount))
    out_plains_01_rough = out_plains_01_rough.filter(ImageFilter.BoxBlur(blur_amount))
    out_hills_01 = out_hills_01.filter(ImageFilter.BoxBlur(blur_amount))
    out_plains_01_dry = out_plains_01_dry.filter(ImageFilter.BoxBlur(blur_amount))

    out_drylands_1_grassy.save('drylands_01_grassy_mask.png')
    out_forest_jungle_1.save('forest_jungle_01_mask.png')
    out_medi_grass_1.save('medi_grass_01_mask.png')
    out_drylands_1_grassy.save('drylands_01_grassy_mask.png')
    out_medi_lumpy_grass.save('medi_lumpy_grass_mask.png')
    out_drylands_1_cracked.save('drylands_01_cracked_mask.png')
    out_desert_cracked.save('desert_cracked_mask.png')
    out_steppe_grass.save('steppe_01_mask.png')
    out_steppe_bushes.save('steppe_bushes_mask.png')
    out_medi_dry_mud.save('medi_dry_mud_mask.png')
    out_medi_noisy_grass.save('medi_noisy_grass_mask.png')
    out_plains_01_noisy.save('plains_01_noisy_mask.png')
    out_plains_01_rough.save('plains_01_rough_mask.png')
    out_hills_01.save('hills_01_mask.png')
    out_plains_01_dry.save('plains_01_dry_mask.png')
    out_beach.save('beach_02_mask.png')


if __name__ == '__main__':
    climate_zones()

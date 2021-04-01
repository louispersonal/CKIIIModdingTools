import csv
import re


class Barony:
    def __init__(self, province_id, name, map_red, map_green, map_blue, localized_name):
        self.province_id = province_id
        self.name = name
        self.map_red = map_red
        self.map_green = map_green
        self.map_blue = map_blue
        self.localized_name = localized_name


class County:

    def __init__(self, name, map_red, map_green, map_blue, localized_name):
        self.name = name
        self.map_red = map_red
        self.map_green = map_green
        self.map_blue = map_blue
        self.baronies = []
        self.localized_name = localized_name

    def add_barony(self, barony):
        self.baronies.append(barony)


class Duchy:

    def __init__(self, name, map_red, map_green, map_blue, localized_name):
        self.name = name
        self.map_red = map_red
        self.map_green = map_green
        self.map_blue = map_blue
        self.counties = []
        self.localized_name = localized_name

    def add_county(self, county):
        self.counties.append(county)


class Kingdom:

    def __init__(self, name, map_red, map_green, map_blue, localized_name):
        self.name = name
        self.map_red = map_red
        self.map_green = map_green
        self.map_blue = map_blue
        self.duchies = []
        self.localized_name = localized_name

    def add_duchy(self, duchy):
        self.duchies.append(duchy)


class Empire:

    def __init__(self, name, map_red, map_green, map_blue, localized_name):
        self.name = name
        self.map_red = map_red
        self.map_green = map_green
        self.map_blue = map_blue
        self.kingdoms = []
        self.localized_name = localized_name

    def add_kingdom(self, kingdom):
        self.kingdoms.append(kingdom)


class LandedTitles:
    def __init__(self):
        self.empires = []

    def add_empire(self, empire):
        self.empires.append(empire)


def create_definition(end_line):
    f = open("definition.csv", "w")
    with open('provinces.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        duplicate_count = 0
        old_barony_name = ""
        for row in csv_reader:
            if line_count == 0 or line_count == 1:
                if line_count == 1:
                    f.write("0;0;0;0;x;x;\n")
            else:
                # province IDs and colors
                province_id = row[0]
                province_red = row[1]
                province_green = row[2]
                province_blue = row[3]

                # baronies
                new_barony_name = row[4]

                if "Sea" in new_barony_name or "Lakey" in new_barony_name or "Impassable" in new_barony_name:
                    if "Sea" in new_barony_name:
                        barony_name_all_caps = re.sub('Sea ', 'sea_', new_barony_name).lower()
                    if "Lake" in new_barony_name:
                        barony_name_all_caps = re.sub('Lakey ', 'lake_', new_barony_name).lower()
                    if "Impassable" in new_barony_name:
                        barony_name_all_caps = re.sub('Impassable ', 'impassable_', new_barony_name).lower()
                else:
                    if new_barony_name == old_barony_name:
                        duplicate_count += 1
                        barony_name_all_caps = re.sub('[\']', '', new_barony_name).upper()
                        barony_name_all_caps = barony_name_all_caps + " " + str(duplicate_count)
                    else:
                        duplicate_count = 0
                        barony_name_all_caps = re.sub('[\']', '', new_barony_name).upper()

                # write to file
                f.write(province_id + ";" + province_red + ";" + province_green + ";" + province_blue + ";"
                        + barony_name_all_caps + ";" + "x;\n")

                old_barony_name = new_barony_name

                if line_count == end_line - 1:
                    break
            line_count += 1
    f.close()
    csv_file.close()


def create_landed_titles(end_line):
    f = open("00_landed_titles.txt", "w")
    landed_titles = LandedTitles()
    with open('provinces.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        duplicate_count = 0
        old_barony_name = ""
        for row in csv_reader:
            if line_count > 1:
                # province ID
                province_id = row[0]

                # baronies (title type 1)
                new_barony_name = row[4]
                barony_name = new_barony_name

                # county (title type 2)
                county_name = row[5]

                # duchy (title type 3)
                duchy_name = row[6]

                # kingdom (title type 4)
                kingdom_name = row[7]

                # empire (title type 5)
                empire_name = row[8]

                # map colors (col 14 15 16)
                map_red = row[14]
                map_green = row[15]
                map_blue = row[16]

                # barony name alteration
                if not ("Sea" in new_barony_name or "Lakey" in new_barony_name or "Impassable" in new_barony_name):
                    if new_barony_name == old_barony_name:
                        duplicate_count += 1
                        barony_name_title = make_name_into_title(new_barony_name, 1)
                        barony_name_title = barony_name_title + "_" + str(duplicate_count)
                        barony_name = barony_name + " " + str(duplicate_count)
                    else:
                        duplicate_count = 0
                        barony_name_title = make_name_into_title(new_barony_name, 1)

                    old_barony_name = new_barony_name

                    # county name alteration
                    county_name_title = make_name_into_title(county_name, 2)

                    # duchy name alteration
                    duchy_name_title = make_name_into_title(duchy_name, 3)

                    # kingdom name alteration
                    kingdom_name_title = make_name_into_title(kingdom_name, 4)

                    # empire name alteration
                    empire_name_title = make_name_into_title(empire_name, 5)

                    # check if empire exists, and create new if not
                    empire_index = check_for_title(landed_titles.empires, empire_name_title)
                    if empire_index == -1:
                        landed_titles.add_empire(Empire(empire_name_title, map_red, map_green, map_blue, empire_name))
                        empire_index = len(landed_titles.empires) - 1

                    # check if kingdom exists, and create new if not
                    empire = landed_titles.empires[empire_index]
                    kingdom_index = check_for_title(empire.kingdoms, kingdom_name_title)
                    if kingdom_index == -1:
                        empire.add_kingdom(Kingdom(kingdom_name_title, map_red, map_green, map_blue, kingdom_name))
                        kingdom_index = len(empire.kingdoms) - 1

                    # check if duchy exists, and create new if not
                    kingdom = empire.kingdoms[kingdom_index]
                    duchy_index = check_for_title(kingdom.duchies, duchy_name_title)
                    if duchy_index == -1:
                        kingdom.add_duchy(Duchy(duchy_name_title, map_red, map_green, map_blue, duchy_name))
                        duchy_index = len(kingdom.duchies) - 1

                    # check if county exists, and create new if not
                    duchy = kingdom.duchies[duchy_index]
                    county_index = check_for_title(duchy.counties, county_name_title)
                    if county_index == -1:
                        duchy.add_county(County(county_name_title, map_red, map_green, map_blue, county_name))
                        county_index = len(duchy.counties) - 1

                    # add barony
                    county = duchy.counties[county_index]
                    county.add_barony(Barony(province_id, barony_name_title, map_red, map_green, map_blue,
                                             barony_name))

                    if line_count == end_line - 1:
                        break

            line_count += 1

    f.write("@correct_culture_primary_score = 100\n@better_than_the_alternatives_score = 50\n"
            "@always_primary_score = 1000\n\n")

    for empire in landed_titles.empires:
        f.write(empire.name + " = {\n\tcolor = { " + empire.map_red + " " + empire.map_green + " " + empire.map_blue +
                " }\n\tcolor2 = { 255 255 255 }\n\n\tcapital = "
                + empire.kingdoms[0].duchies[0].counties[0].name + "\n\n")
        for kingdom in empire.kingdoms:
            f.write("\t" + kingdom.name + " = {\n\t\tcolor = { " + kingdom.map_red + " " + kingdom.map_green + " " +
                    kingdom.map_blue + " }\n\t\tcolor2 = { 255 255 255 }\n\n\t\tcapital = "
                    + kingdom.duchies[0].counties[0].name + "\n\n")
            for duchy in kingdom.duchies:
                f.write("\t\t" + duchy.name + " = {\n\t\t\tcolor = { " + duchy.map_red + " " + duchy.map_green + " " +
                        duchy.map_blue + " }\n\t\t\tcolor2 = { 255 255 255 }\n\n\t\t\tcapital = "
                        + duchy.counties[0].name + "\n\n")
                for county in duchy.counties:
                    f.write("\t\t\t" + county.name + " = {\n\t\t\t\tcolor = { " + county.map_red + " " +
                            county.map_green + " " + county.map_blue + " }\n\t\t\t\tcolor2 = { 255 255 255 }\n\n")
                    for barony in county.baronies:
                        f.write("\t\t\t\t" + barony.name + " = {\n\t\t\t\t\tprovince = " + barony.province_id +
                                "\n\t\t\t\t\tcolor = { " + barony.map_red + " " + barony.map_green + " " +
                                barony.map_blue + " }\n\t\t\t\t\tcolor2 = { 255 255 255 }\n\n\t\t\t\t}\n")
                    f.write("\n\t\t\t}\n")
                f.write("\n\t\t}\n")
            f.write("\n\t}\n")
        f.write("\n}\n")

    f.close()

    f2 = open("titles_l_english.yml", "w")

    f2.write(
        "l_english:\n TITLE_NAME:0 \"$NAME$\"\n TITLE_TIERED_NAME:0 \"$TIER|U$ of $NAME$\"\n TITLE_CLAN_TIERED_NAME"
        ":0 \"the $NAME$ $TIER|U$\"\n TITLE_CLAN_TIERED_WITH_UNDERLYING_NAME:0 \"the $NAME$ $TIER|U$ #F ($TIER|U$ "
        "of $BASE_NAME$) #!\"\n TITLE_TIER_AS_NAME:0 \"$TIER|U$\"\n\n\n")

    for empire in landed_titles.empires:
        f2.write(" " + empire.name + ":0 \"" + empire.localized_name + "\"\n")
        for kingdom in empire.kingdoms:
            f2.write(" " + kingdom.name + ":0 \"" + kingdom.localized_name + "\"\n")
            for duchy in kingdom.duchies:
                f2.write(" " + duchy.name + ":0 \"" + duchy.localized_name + "\"\n")
                for county in duchy.counties:
                    f2.write(" " + county.name + ":0 \"" + county.localized_name + "\"\n")
                    for barony in county.baronies:
                        f2.write(" " + barony.name + ":0 \"" + barony.localized_name + "\"\n")

    f2.close()
    csv_file.close()


def make_name_into_title(name, title_type):
    name = re.sub('[\']', '', name).lower()
    name = re.sub('[ ]', '_', name)
    if title_type == 1:
        return "b_" + name
    if title_type == 2:
        return "c_" + name
    if title_type == 3:
        return "d_" + name
    if title_type == 4:
        return "k_" + name
    if title_type == 5:
        return "e_" + name


def check_for_title(title_list, title_name):
    index = -1
    i = 0
    for title in title_list:
        if title.name == title_name:
            index = i
        i = i + 1
    return index


def print_landed_titles(landed_title_list):
    for empire in landed_title_list.empires:
        print(empire.name)
        for kingdom in empire.kingdoms:
            print('\t' + kingdom.name)
            for duchy in kingdom.duchies:
                print('\t\t' + duchy.name)
                for county in duchy.counties:
                    print('\t\t\t' + county.name)
                    for barony in county.baronies:
                        print('\t\t\t\t' + barony.name)


def make_color_palette(start_line, end_line):
    start_line = start_line - 1
    f = open("provinces.gpl", "w")
    f.write("GIMP Palette\nName: provinces\nColumns: 0\n#\n")
    with open('provinces.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        duplicate_count = 0
        old_barony_name = ""
        for row in csv_reader:
            if line_count >= start_line:
                # province IDs and colors
                province_red = row[1]
                province_green = row[2]
                province_blue = row[3]

                # baronies
                new_barony_name = row[4]

                if "Sea" in new_barony_name:
                    barony_name_all_caps = re.sub('Sea ', 'sea_', new_barony_name).lower()
                else:
                    if new_barony_name == old_barony_name:
                        duplicate_count += 1
                        barony_name_all_caps = re.sub('[\']', '', new_barony_name).upper()
                        barony_name_all_caps = barony_name_all_caps + " " + str(duplicate_count)
                    else:
                        duplicate_count = 0
                        barony_name_all_caps = re.sub('[\']', '', new_barony_name).upper()

                # write to file
                f.write(make_integer_three_spaces(province_red) + " " + make_integer_three_spaces(province_green) +
                        " " + make_integer_three_spaces(province_blue) + " " + barony_name_all_caps + "\n")

                old_barony_name = new_barony_name

                if line_count == end_line - 1:
                    break
            line_count += 1
    f.close()
    csv_file.close()


def make_integer_three_spaces(num):
    if int(num) < 10:
        return "  " + num
    if int(num) < 100:
        return " " + num
    if int(num) > 99:
        return


# make history/provinces
def make_province_history(end_line):
    f = open("k_all.txt", "w")
    with open('provinces.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count >= 2:
                province_id = row[0]
                province_culture = row[10]
                province_religion = row[11]
                province_holding = row[13]
                f.write(str(province_id) + " = {\n\tculture = " + province_culture + "\n\treligion = " + province_religion
                        + "\n\tholding = " + province_holding + "\n}\n")
                if line_count == end_line - 1:
                    break
            line_count += 1
    f.close()
    csv_file.close()


# make history/titles


# make province terrain
def make_province_terrain(end_line):
    f = open("00_province_terrain.txt", "w")
    f.write("# plains, forest, mountains, hills, wetlands, taiga, drylands, desert, desert_mountains, farmlands,"
            " floodplains, oasis\n\n")
    with open('provinces.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count >= 2:
                province_id = row[0]
                province_name = row[4]
                province_terrain = row[9]
                if not ("Sea" in province_name or "Lakey" in province_name or "Impassable" in province_name):
                    f.write(str(province_id) + "=" + province_terrain + "\n")
                if line_count == end_line - 1:
                    break
            line_count += 1
    f.close()
    csv_file.close()


if __name__ == '__main__':
    print("Welcome to the CKIII tools thing. What do you want to do?\n")
    print("1. Landed Titles\n2. Definition\n3. Color Palette\n4. Province History\n5. Province Terrain")
    choice = input("Input your choice: ")
    if int(choice) == 1:
        end_line = input("What's the last line of your csv you want to compute? ")
        create_landed_titles(int(end_line))
    if int(choice) == 2:
        end_line = input("What's the last line of your csv you want to compute? ")
        create_definition(int(end_line))
    if int(choice) == 3:
        start_line = input("What's the first line of your csv you want to compute? ")
        end_line = input("What's the last line of your csv you want to compute? ")
        make_color_palette(int(start_line), int(end_line))
    if int(choice) == 4:
        end_line = input("What's the last line of your csv you want to compute? ")
        make_province_history(int(end_line))
    if int(choice) == 5:
        end_line = input("What's the last line of your csv you want to compute? ")
        make_province_terrain(int(end_line))
    # create_landed_titles(3106)
    # need to fix landed titles creation to avoid lakes and impassables
    # create_definition(3106)
    # make_color_palette(2910, 2987)
    # make_province_history(10)
    # make_province_terrain(2988)

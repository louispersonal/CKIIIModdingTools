import csv
import random
import re


class Character:
    def __init__(self, character_number, name, dynasty_name, religion, culture, dynasties, dynasty_culture, textured,
                 background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1, icon_color_2, icon_color_3,
                 female, birth):
        self.character_number = character_number
        self.name = name
        self.religion = religion
        self.culture = culture
        self.female = female
        self.birth = birth

        self.dynasty_number = dynasties.find_dynasty(dynasty_name, dynasty_culture, textured, background, bg_color_1,
                                                     bg_color_2, bg_color_3, icon, icon_color_1, icon_color_2,
                                                     icon_color_3)


class Dynasty:
    def __init__(self, name, culture, textured, background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1,
                 icon_color_2, icon_color_3):
        self.name = name
        self.culture = culture
        self.coat = CoatOfArms(textured, background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1,
                               icon_color_2, icon_color_3)

    def get_prefix(self):
        if "_" in self.name:
            return self.name.split("_")[0]
        return "no prefix"

    def get_name(self):
        if "_" in self.name:
            return self.name.split("_")[1]
        return self.name


class DynastyList:
    def __init__(self):
        self.dynasties = []
        self.dynasties.append(Dynasty("none", "none", "x", "x", "x", "x", "x", "x", "x", "x", "x"))

    def find_dynasty(self, name, culture, textured, background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1,
                     icon_color_2, icon_color_3):
        index = 0
        for dynasty in self.dynasties:
            if dynasty.name == name:
                return index
        self.dynasties.append(Dynasty(name, culture, textured, background, bg_color_1, bg_color_2, bg_color_3,
                                      icon, icon_color_1, icon_color_2, icon_color_3))
        return len(self.dynasties) - 1


class CoatOfArms:
    def __init__(self, textured, background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1,
                 icon_color_2, icon_color_3):
        self.textured = textured
        self.background = background
        self.bg_color_1 = bg_color_1
        self.bg_color_2 = bg_color_2
        self.bg_color_3 = bg_color_3
        self.icon = icon
        self.icon_color_1 = icon_color_1
        self.icon_color_2 = icon_color_2
        self.icon_color_3 = icon_color_3

    def check_if_empty(self):
        if self.textured == "x" and self.background == "x":
            return True
        else:
            return False

    def check_if_textured(self):
        if self.check_if_empty():
            return False
        else:
            if self.textured == "x":
                return False
            else:
                return True

    def write_coat_of_arms(self, numeric_id):
        if self.check_if_empty():
            return ""
        else:
            if self.check_if_textured():
                coat_string = str(numeric_id) + " = {\n\tpattern = \"pattern_solid.dds\"\n\tcolor1 = \"white\"\n" \
                                                "\ttextured_emblem = {\n\t\ttexture = " + self.textured \
                              + ".dds\n\t}\n}\n\n"
            else:
                coat_string = str(numeric_id) + " = {\n\tpattern = \"" + self.background + ".dds\"\n\tcolor1 = \"" \
                              + self.bg_color_1 + "\"\n\t"
                if not self.bg_color_2 == "x":
                    coat_string = coat_string + "\tcolor2 = \"" + self.bg_color_2 + "\"\n"
                if not self.bg_color_3 == "x":
                    coat_string = coat_string + "\tcolor3 = \"" + self.bg_color_3 + "\"\n"
                coat_string = coat_string + "\tcolored_emblem = {\n\t\ttexture = \"" + self.icon + \
                                            ".dds\"\n\t\tcolor1 = \"" + self.icon_color_1 + "\"\n"
                if not self.icon_color_2 == "x":
                    coat_string = coat_string + "\t\tcolor2 = \"" + self.icon_color_2 + "\"\n"
                if not self.icon_color_3 == "x":
                    coat_string = coat_string + "\t\tcolor3 = \"" + self.icon_color_3 + "\"\n"
                coat_string = coat_string + "\t\t}\n}\n\n"
            return coat_string


class Barony:
    def __init__(self, province_id, name, map_red, map_green, map_blue, localized_name, terrain, culture, religion,
                 holding):
        self.province_id = province_id
        self.name = name
        self.map_red = map_red
        self.map_green = map_green
        self.map_blue = map_blue
        self.localized_name = localized_name
        self.terrain = terrain
        self.culture = culture
        self.religion = religion
        self.holding = holding
        self.is_capital = False

    def set_as_capital(self):
        self.is_capital = True


class County:

    def __init__(self, name, map_red, map_green, map_blue, localized_name):
        self.name = name
        self.map_red = map_red
        self.map_green = map_green
        self.map_blue = map_blue
        self.baronies = []
        self.localized_name = localized_name
        self.capital = None
        self.holder = 0
        self.year = 2660
        self.liege = "none"
        self.coat = None
        self.government = "x"

    def add_barony(self, barony):
        self.baronies.append(barony)
        if len(self.baronies) == 1:
            self.capital = self.baronies[0]
            self.baronies[0].set_as_capital()

    def assign_holder(self, holder, year, liege):
        self.holder = holder
        self.year = year
        self.liege = liege

    def set_red(self, map_red):
        if map_red > 255:
            self.map_red = 255
        else:
            if map_red < 0:
                self.map_red = 0
            else:
                self.map_red = map_red

    def set_green(self, map_green):
        if map_green > 255:
            self.map_green = 255
        else:
            if map_green < 0:
                self.map_green = 0
            else:
                self.map_green = map_green

    def set_blue(self, map_blue):
        if map_blue > 255:
            self.map_blue = 255
        else:
            if map_blue < 0:
                self.map_blue = 0
            else:
                self.map_blue = map_blue

    def set_coat(self, textured, background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1,
                 icon_color_2, icon_color_3):
        self.coat = CoatOfArms(textured, background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1,
                               icon_color_2, icon_color_3)

    def set_government(self, government):
        self.government = government


class Duchy:

    def __init__(self, name, map_red, map_green, map_blue, localized_name):
        self.name = name
        self.map_red = map_red
        self.map_green = map_green
        self.map_blue = map_blue
        self.counties = []
        self.localized_name = localized_name
        self.holder = 0
        self.year = 2660
        self.liege = "none"
        self.coat = None
        self.government = "x"

    def add_county(self, county):
        self.counties.append(county)

    def set_red(self, map_red):
        if map_red > 255:
            self.map_red = 255
        else:
            if map_red < 0:
                self.map_red = 0
            else:
                self.map_red = map_red

    def set_green(self, map_green):
        if map_green > 255:
            self.map_green = 255
        else:
            if map_green < 0:
                self.map_green = 0
            else:
                self.map_green = map_green

    def set_blue(self, map_blue):
        if map_blue > 255:
            self.map_blue = 255
        else:
            if map_blue < 0:
                self.map_blue = 0
            else:
                self.map_blue = map_blue

    def assign_holder(self, holder, year, liege):
        self.holder = holder
        self.year = year
        self.liege = liege

    def set_coat(self, textured, background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1,
                 icon_color_2, icon_color_3):
        self.coat = CoatOfArms(textured, background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1,
                               icon_color_2, icon_color_3)

    def set_government(self, government):
        self.government = government


class Kingdom:

    def __init__(self, name, map_red, map_green, map_blue, localized_name):
        self.name = name
        self.map_red = map_red
        self.map_green = map_green
        self.map_blue = map_blue
        self.duchies = []
        self.localized_name = localized_name
        self.holder = 0
        self.year = 2660
        self.liege = "none"
        self.coat = None
        self.government = "x"

    def add_duchy(self, duchy):
        self.duchies.append(duchy)

    def assign_holder(self, holder, year, liege):
        self.holder = holder
        self.year = year
        self.liege = liege

    def set_coat(self, textured, background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1,
                 icon_color_2, icon_color_3):
        self.coat = CoatOfArms(textured, background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1,
                               icon_color_2, icon_color_3)

    def set_government(self, government):
        self.government = government


class Empire:

    def __init__(self, name, map_red, map_green, map_blue, localized_name):
        self.name = name
        self.map_red = map_red
        self.map_green = map_green
        self.map_blue = map_blue
        self.kingdoms = []
        self.localized_name = localized_name
        self.holder = 0
        self.year = 2660
        self.liege = "none"
        self.coat = None
        self.government = "x"

    def add_kingdom(self, kingdom):
        self.kingdoms.append(kingdom)

    def assign_holder(self, holder, year, liege):
        self.holder = holder
        self.year = year
        self.liege = liege

    def set_coat(self, textured, background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1,
                 icon_color_2, icon_color_3):
        self.coat = CoatOfArms(textured, background, bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1,
                               icon_color_2, icon_color_3)

    def set_government(self, government):
        self.government = government


class LandedTitles:
    def __init__(self):
        self.empires = []

    def add_empire(self, empire):
        self.empires.append(empire)


def create_landed_titles_object(end_line):
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

                # terrain
                terrain = row[9]

                # culture
                culture = row[10]

                # religion
                religion = row[11]

                # holding
                holding = row[12]

                # map colors
                map_red = row[13]
                map_green = row[14]
                map_blue = row[15]

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
                        kingdom.add_duchy(Duchy(duchy_name_title, 255, 255, 255, duchy_name))
                        duchy_index = len(kingdom.duchies) - 1

                    # check if county exists, and create new if not
                    duchy = kingdom.duchies[duchy_index]
                    county_index = check_for_title(duchy.counties, county_name_title)
                    if county_index == -1:
                        duchy.add_county(County(county_name_title, 255, 255, 255, county_name))
                        county_index = len(duchy.counties) - 1

                    # add barony
                    county = duchy.counties[county_index]
                    county.add_barony(Barony(province_id, barony_name_title, 255, 255, 255,
                                             barony_name, terrain, culture, religion, holding))

                    if line_count == end_line - 1:
                        break

            line_count += 1

    csv_file.close()
    apply_title_colors(landed_titles)
    return landed_titles


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


def write_landed_titles_file(landed_titles):
    f = open("landed_titles/00_landed_titles.txt", "w")
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
                f.write("\t\t" + duchy.name + " = {\n\t\t\tcolor = { " + str(duchy.map_red) + " " + str(
                    duchy.map_green) + " " +
                        str(duchy.map_blue) + " }\n\t\t\tcolor2 = { 255 255 255 }\n\n\t\t\tcapital = "
                        + duchy.counties[0].name + "\n\n")
                for county in duchy.counties:
                    f.write("\t\t\t" + county.name + " = {\n\t\t\t\tcolor = { " + str(county.map_red) + " " +
                            str(county.map_green) + " " + str(
                        county.map_blue) + " }\n\t\t\t\tcolor2 = { 255 255 255 }\n\n")
                    for barony in county.baronies:
                        f.write("\t\t\t\t" + barony.name + " = {\n\t\t\t\t\tprovince = " + str(barony.province_id) +
                                "\n\t\t\t\t\tcolor = { " + str(barony.map_red) + " " + str(barony.map_green) + " " +
                                str(barony.map_blue) + " }\n\t\t\t\t\tcolor2 = { 255 255 255 }\n\n\t\t\t\t}\n")
                    f.write("\n\t\t\t}\n")
                f.write("\n\t\t}\n")
            f.write("\n\t}\n")
        f.write("\n}\n")

    f.close()


def write_titles_localization(landed_titles):
    f = open("localization/titles_l_english.yml", "w", encoding="utf8")

    f.write(
        "l_english:\n TITLE_NAME:0 \"$NAME$\"\n TITLE_TIERED_NAME:0 \"$TIER|U$ of $NAME$\"\n TITLE_CLAN_TIERED_NAME"
        ":0 \"the $NAME$ $TIER|U$\"\n TITLE_CLAN_TIERED_WITH_UNDERLYING_NAME:0 \"the $NAME$ $TIER|U$ #F ($TIER|U$ "
        "of $BASE_NAME$) #!\"\n TITLE_TIER_AS_NAME:0 \"$TIER|U$\"\n\n\n")

    for empire in landed_titles.empires:
        if empire.name == "e_murrurnitja":
            f.write(" " + empire.name + ":0 \"" + localize_murrurnitja_name(empire.localized_name) + "\"\n")
        else:
            f.write(" " + empire.name + ":0 \"" + empire.localized_name + "\"\n")
        for kingdom in empire.kingdoms:
            if empire.name == "e_murrurnitja":
                f.write(" " + kingdom.name + ":0 \"" + localize_murrurnitja_name(kingdom.localized_name) + "\"\n")
            else:
                f.write(" " + kingdom.name + ":0 \"" + kingdom.localized_name + "\"\n")
            for duchy in kingdom.duchies:
                if empire.name == "e_murrurnitja":
                    f.write(" " + duchy.name + ":0 \"" + localize_murrurnitja_name(duchy.localized_name) + "\"\n")
                else:
                    f.write(" " + duchy.name + ":0 \"" + duchy.localized_name + "\"\n")
                for county in duchy.counties:
                    if empire.name == "e_murrurnitja":
                        f.write(" " + county.name + ":0 \"" + localize_murrurnitja_name(county.localized_name) + "\"\n")
                    else:
                        f.write(" " + county.name + ":0 \"" + county.localized_name + "\"\n")
                    for barony in county.baronies:
                        if empire.name == "e_murrurnitja":
                            f.write(" " + barony.name + ":0 \"" + localize_murrurnitja_name(barony.localized_name) + "\"\n")
                        else:
                            f.write(" " + barony.name + ":0 \"" + barony.localized_name + "\"\n")

    f.close()


def localize_murrurnitja_name(m_name):
    word = m_name.lower()
    new_word = [""]
    for letter in word:
        if letter == "d" or letter == "t":
            new_word.append("đ")
        elif letter == "j":
            new_word[-1] = "ĵ"
        elif letter == "y":
            if new_word[-1] == "n":
                new_word[-1] = "ņ"
            elif new_word[-1] == "l":
                new_word[-1] = "ŀ"
            else:
                new_word.append(letter)
        elif letter == "g":
            if new_word[-1] == "n":
                new_word[-1] = "ŋ"
            else:
                new_word.append(letter)
        elif letter == "l":
            if new_word[-1] == "r":
                new_word[-1] = "ļ"
            else:
                new_word.append(letter)
        elif letter == "r":
            if new_word[-1] == "r":
                new_word[-1] = "ř"
            else:
                new_word.append(letter)
        elif letter == "o":
            if new_word[-1] == "o":
                new_word[-1] = "u"
            else:
                new_word.append(letter)
        elif letter == "a":
            if new_word[-1] == "a":
                new_word[-1] = "ā"
            else:
                new_word.append(letter)
        else:
            new_word.append(letter)

    new_word_string = ""
    for item in new_word:
        new_word_string = new_word_string + item

    return new_word_string.capitalize()


def write_province_history(landed_titles):
    f = open("provinces/k_all.txt", "w")
    for empire in landed_titles.empires:
        f.write("# " + empire.name + "\n")
        for kingdom in empire.kingdoms:
            f.write("# " + kingdom.name + "\n")
            for duchy in kingdom.duchies:
                f.write("# " + duchy.name + "\n")
                for county in duchy.counties:
                    f.write("### " + county.name + "\n")
                    for barony in county.baronies:
                        if barony.is_capital:
                            f.write(str(barony.province_id) + " = {  #" + barony.localized_name + "\n\tculture = " +
                                    barony.culture + "\n\treligion = " + barony.religion + "\n\tholding = " +
                                    barony.holding + "\n}\n\n")
                        else:
                            f.write(str(barony.province_id) + " = {  #" + barony.localized_name + "\n\tholding = " +
                                    barony.holding + "\n}\n\n")
    f.close()


def write_province_terrains(landed_titles):
    f = open("province_terrain/00_province_terrain.txt", "w")
    f.write("# plains, forest, mountains, hills, wetlands, taiga, drylands, desert, desert_mountains, farmlands,"
            " floodplains, oasis\n\n")
    for empire in landed_titles.empires:
        for kingdom in empire.kingdoms:
            for duchy in kingdom.duchies:
                for county in duchy.counties:
                    for barony in county.baronies:
                        f.write(str(barony.province_id) + "=" + barony.terrain + "\n")
    f.close()


def initialize_title_character_list(landed_titles):
    f = open("titles_characters.csv", "w")
    f.write("title,character number,year,liege,textured emblem,background,bg color 1,bg color 2,bg color 3,icon,"
            "icon color 1,icon color 2,icon color 3,government\n")
    for empire in landed_titles.empires:
        f.write(empire.name + "," + str(empire.holder) + "\n")
        for kingdom in empire.kingdoms:
            f.write(kingdom.name + "," + str(kingdom.holder) + "\n")
            for duchy in kingdom.duchies:
                f.write(duchy.name + "," + str(duchy.holder) + "\n")
                for county in duchy.counties:
                    f.write(county.name + "," + str(county.holder) + "\n")
    f.close()


def title_character_coat_assignment(landed_titles):
    with open('titles_characters.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                # file read
                title = row[0]
                character_number = row[1]
                year = row[2]
                liege = row[3]
                textured_emblem = row[4]
                background = row[5]
                bg_color_1 = row[6]
                bg_color_2 = row[7]
                bg_color_3 = row[8]
                icon = row[9]
                icon_color_1 = row[10]
                icon_color_2 = row[11]
                icon_color_3 = row[12]
                government = row[13]

                index = -1

                if title[0:2] == "e_":
                    index = check_for_title(landed_titles.empires, title)
                    landed_titles.empires[index].assign_holder(character_number, year, liege)
                    landed_titles.empires[index].set_coat(textured_emblem, background, bg_color_1, bg_color_2,
                                                          bg_color_3, icon, icon_color_1, icon_color_2, icon_color_3)
                    landed_titles.empires[index].set_government(government)
                if title[0:2] == "k_":
                    for empire in landed_titles.empires:
                        for kingdom in empire.kingdoms:
                            index = check_for_title(empire.kingdoms, title)
                            if index >= 0:
                                empire.kingdoms[index].assign_holder(character_number, year, liege)
                                empire.kingdoms[index].set_coat(textured_emblem, background, bg_color_1, bg_color_2,
                                                                bg_color_3, icon, icon_color_1, icon_color_2,
                                                                icon_color_3)
                                empire.kingdoms[index].set_government(government)
                if title[0:2] == "d_":
                    for empire in landed_titles.empires:
                        for kingdom in empire.kingdoms:
                            for duchy in kingdom.duchies:
                                index = check_for_title(kingdom.duchies, title)
                                if index >= 0:
                                    kingdom.duchies[index].assign_holder(character_number, year, liege)
                                    kingdom.duchies[index].set_coat(textured_emblem, background, bg_color_1,
                                                                    bg_color_2, bg_color_3, icon, icon_color_1,
                                                                    icon_color_2, icon_color_3)
                                    kingdom.duchies[index].set_government(government)
                if title[0:2] == "c_":
                    for empire in landed_titles.empires:
                        for kingdom in empire.kingdoms:
                            for duchy in kingdom.duchies:
                                for county in duchy.counties:
                                    index = check_for_title(duchy.counties, title)
                                    if index >= 0:
                                        duchy.counties[index].assign_holder(character_number, year, liege)
                                        duchy.counties[index].set_coat(textured_emblem, background, bg_color_1,
                                                                       bg_color_2, bg_color_3, icon, icon_color_1,
                                                                       icon_color_2, icon_color_3)
                                        duchy.counties[index].set_government(government)
            line_count = line_count + 1
    csv_file.close()


def write_title_history(landed_titles):
    f = open("titles/k_all.txt", "w")

    for empire in landed_titles.empires:
        if not empire.holder == 0:
            f.write(empire.name + " = {\n\t" + str(empire.year) + ".1.1 = {\n\t\tholder = "
                    + str(empire.holder) + "\n")
            if not empire.liege == "none":
                f.write("\t\tliege = \"" + empire.liege + "\"\n")
            if not empire.government == "x":
                f.write("\t\tgovernment = \"" + empire.government + "\"\n")
            f.write("\t}\n}\n\n")

        for kingdom in empire.kingdoms:
            if not kingdom.holder == 0:
                f.write(kingdom.name + " = {\n\t" + str(kingdom.year) + ".1.1 = {\n\t\tholder = "
                        + str(kingdom.holder) + "\n")
                if not kingdom.liege == "none":
                    f.write("\t\tliege = \"" + kingdom.liege + "\"\n")
                if not kingdom.government == "x":
                    f.write("\t\tgovernment = \"" + kingdom.government + "\"\n")
                f.write("\t}\n}\n\n")

            for duchy in kingdom.duchies:
                if not duchy.holder == 0:
                    f.write(duchy.name + " = {\n\t" + str(duchy.year) + ".1.1 = {\n\t\tholder = "
                            + str(duchy.holder) + "\n")
                    if not duchy.liege == "none":
                        f.write("\t\tliege = \"" + duchy.liege + "\"\n")
                    if not duchy.government == "x":
                        f.write("\t\tgovernment = \"" + duchy.government + "\"\n")
                    f.write("\t}\n}\n\n")

                for county in duchy.counties:
                    if not county.holder == 0:
                        f.write(county.name + " = {\n\t" + str(county.year) + ".1.1 = {\n\t\tholder = "
                                + str(county.holder) + "\n")
                        if not county.liege == "none":
                            f.write("\t\tliege = \"" + county.liege + "\"\n")
                        if not county.government == "x":
                            f.write("\t\tgovernment = \"" + county.government + "\"\n")
                        f.write("\t}\n}\n\n")
    f.close()


def write_title_history_modified(landed_titles):

    for empire in landed_titles.empires:
        f_e = open("titles/"+empire.name+".txt", "w")
        if not empire.holder == 0:
            f_e.write(empire.name + " = {\n\t" + str(empire.year) + ".1.1 = {\n\t\tholder = "
                      + str(empire.holder) + "\n")
            if not empire.liege == "none":
                f_e.write("\t\tliege = \"" + empire.liege + "\"\n")
            if not empire.government == "x":
                f_e.write("\t\tgovernment = \"" + empire.government + "\"\n")
            f_e.write("\t}\n}\n\n")

        for kingdom in empire.kingdoms:
            f = open("titles/" + kingdom.name + ".txt", "w")
            if not kingdom.holder == 0:
                f.write(kingdom.name + " = {\n\t" + str(kingdom.year) + ".1.1 = {\n\t\tholder = "
                        + str(kingdom.holder) + "\n")
                if not kingdom.liege == "none":
                    f.write("\t\tliege = \"" + kingdom.liege + "\"\n")
                if not kingdom.government == "x":
                    f.write("\t\tgovernment = \"" + kingdom.government + "\"\n")
                f.write("\t}\n}\n\n")

            for duchy in kingdom.duchies:
                if not duchy.holder == 0:
                    f.write(duchy.name + " = {\n\t" + str(duchy.year) + ".1.1 = {\n\t\tholder = "
                            + str(duchy.holder) + "\n")
                    if not duchy.liege == "none":
                        f.write("\t\tliege = \"" + duchy.liege + "\"\n")
                    if not duchy.government == "x":
                        f.write("\t\tgovernment = \"" + duchy.government + "\"\n")
                    f.write("\t}\n}\n\n")

                for county in duchy.counties:
                    if not county.holder == 0:
                        f.write(county.name + " = {\n\t" + str(county.year) + ".1.1 = {\n\t\tholder = "
                                + str(county.holder) + "\n")
                        if not county.liege == "none":
                            f.write("\t\tliege = \"" + county.liege + "\"\n")
                        if not county.government == "x":
                            f.write("\t\tgovernment = \"" + county.government + "\"\n")
                        f.write("\t}\n}\n\n")
        f_e.close()


def apply_title_colors(landed_titles):
    for empire in landed_titles.empires:
        for kingdom in empire.kingdoms:
            colors = [int(kingdom.map_red), int(kingdom.map_green), int(kingdom.map_blue)]
            index, is_small = find_biggest_smallest_number(colors)
            for duchy in kingdom.duchies:
                duchy.set_red(colors[0])
                duchy.set_green(colors[1])
                duchy.set_blue(colors[2])
                for county in duchy.counties:
                    county.set_red(colors[0])
                    county.set_green(colors[1])
                    county.set_blue(colors[2])
                    modify_color(colors, index, is_small)


def find_biggest_smallest_number(colors):
    smallest = min(colors)
    biggest = max(colors)
    if smallest < (255 - biggest):
        return colors.index(smallest), True
    else:
        return colors.index(biggest), False


def modify_color(colors, index, is_small):
    if is_small:
        colors[index] = colors[index] + 2
    else:
        colors[index] = colors[index] - 2
    return colors


def character_creation():
    with open('character_master.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        characters = []
        dynasties = DynastyList()
        for row in csv_reader:
            if line_count > 0:
                character_number = row[0]
                character_name = row[1]
                dynasty_name = row[2]
                religion = row[3]
                character_culture = row[4]
                dynasty_culture = row[5]
                textured_emblem = row[6]
                background = row[7]
                bg_color_1 = row[8]
                bg_color_2 = row[9]
                bg_color_3 = row[10]
                icon = row[11]
                icon_color_1 = row[12]
                icon_color_2 = row[13]
                icon_color_3 = row[14]
                female = row[15]
                birth = row[16]

                characters.append(Character(character_number, character_name, dynasty_name, religion,
                                            character_culture, dynasties, dynasty_culture, textured_emblem, background,
                                            bg_color_1, bg_color_2, bg_color_3, icon, icon_color_1, icon_color_2,
                                            icon_color_3, female, birth))
            line_count = line_count + 1
    csv_file.close()
    return characters, dynasties


# write character history
def write_character_history(characters):
    f = open("characters/all.txt", "w")

    for character in characters:
        f.write(str(character.character_number) + " = {\n\tname = \"" + character.name + "\"\n")
        if character.female == "yes":
            f.write("\tfemale = yes\n")
        f.write("\tdynasty = " + str(character.dynasty_number) + "\n")
        f.write("\treligion = \"" + character.religion + "\"\n")
        f.write("\tculture = \"" + character.culture + "\"\n")
        f.write("\t" + str(character.birth) + "." + str(random.randint(1, 12)) + "." + str(random.randint(1, 28))
                + " = {\n\t\tbirth = yes\n\t}\n")
        f.write("}\n\n")


# write dynasties
def write_dynasties(dynasty_list):
    f = open("dynasties/00_dynasties.txt", "w")

    dynasties = dynasty_list.dynasties
    line_count = 0
    for dynasty in dynasties:
        if line_count > 0:
            f.write(str(line_count) + " = {\n")
            if not dynasty.get_prefix() == "no prefix":
                f.write("\tprefix = \"dynnp_" + dynasty.get_prefix() + "\"\n")
            f.write("\tname = \"dynn_" + dynasty.get_name() + "\"\n")
            f.write("\tculture = \"" + dynasty.culture + "\"\n")
            f.write("}\n")
        line_count = line_count + 1


# write coat of arms for titles
def write_title_coats(landed_titles):
    f = open("coat_of_arms/01_landed_titles.txt", "w")

    for empire in landed_titles.empires:
        f.write(empire.coat.write_coat_of_arms(empire.name))

        for kingdom in empire.kingdoms:
            f.write(kingdom.coat.write_coat_of_arms(kingdom.name))

            for duchy in kingdom.duchies:
                f.write(duchy.coat.write_coat_of_arms(duchy.name))

                for county in duchy.counties:
                    f.write(county.coat.write_coat_of_arms(county.name))

    f.close()


# write coat of arms for titles
def write_dynasty_coats(dynasty_list):
    f = open("coat_of_arms/90_dynasties.txt", "w")
    dynasties = dynasty_list.dynasties

    line_count = 0
    for dynasty in dynasties:
        if line_count > 0:
            f.write(dynasty.coat.write_coat_of_arms(line_count))
        line_count = line_count + 1

    f.close()


if __name__ == '__main__':
    # read provinces file and create title objects from it
    titles = create_landed_titles_object(2969)

    # read titles_characters file and assign holders and coats to titles
    title_character_coat_assignment(titles)

    # read character master file and create characters and dynasties
    master_characters, master_dynasties = character_creation()

    # make the dynasty coat of arms file
    write_dynasty_coats(master_dynasties)

    # make the title coat of arms file
    write_title_coats(titles)

    # write dynasty file
    write_dynasties(master_dynasties)

    # write character file
    write_character_history(master_characters)

    # write landed titles file
    write_landed_titles_file(titles)

    # write province history file
    write_province_history(titles)

    # write province terrain file
    write_province_terrains(titles)

    # write title history
    write_title_history_modified(titles)

    # localization
    write_titles_localization(titles)

    # initialize_title_character_list(titles)


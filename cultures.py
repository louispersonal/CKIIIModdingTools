import csv


def culture_creation():
    f = open("cultures/00_wanjinawunggurr.txt", "w", encoding="utf8")
    with open('culture_templates/wanjinawunggurr.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        section_line_count = 0
        ethnicities = []
        for row in csv_reader:
            if line_count > 0:
                if line_count < 7:
                    if line_count == 1:
                        f.write(row[1] + " = {\n\n")
                    if line_count == 2:
                        mercenaries = row[1].split()
                        f.write("\tmercenary_names = {\n")
                        for mercenary in mercenaries:
                            f.write("\t\t{ name = \"mercenary_company_" + mercenary + "\" }\n")
                        f.write("\t}\n\n")
                    if line_count == 3:
                        group_coa = row[1]
                    if line_count == 4:
                        group_building = row[1]
                    if line_count == 5:
                        group_clothing = row[1]
                    if line_count == 6:
                        group_unit = row[1]
                        f.write("\tgraphical_cultures = {\n\t\t" + group_coa + "\n")
                        f.write("\t\t" + group_building + "\n")
                        f.write("\t\t" + group_clothing + "\n")
                        f.write("\t\t" + group_unit + "\n")
                        f.write("\t}\n\n")
                else:
                    if section_line_count == 0:
                        f.write("\t" + row[1] + " = {\n")
                    if section_line_count == 1:
                        f.write("\t\tgraphical_cultures = {\n\t\t\t" + row[1] + "\n\t\t}\n\n")
                    if section_line_count == 2:
                        s_mercenaries = row[1].split()
                        f.write("\t\tmercenary_names = {\n")
                        for s_mercenary in s_mercenaries:
                            f.write("\t\t\t{ name = \"mercenary_company_" + s_mercenary + "\" }\n")
                        f.write("\t\t}\n\n")
                    if section_line_count == 3:
                        f.write("\t\tcolor = { " + row[1] + " }\n\n")
                    if section_line_count == 5:
                        f.write("\t\tmale_names = {\n\t\t\t" + row[1] + "\n\t\t}\n")
                    if section_line_count == 6:
                        f.write("\t\tfemale_names = {\n\t\t\t" + row[1] + "\n\t\t}\n")
                    if section_line_count == 7:
                        cadet_dynasties = row[1].split()
                        f.write("\t\tcadet_dynasty_names = {\n")
                        for cadet_dynasty in cadet_dynasties:
                            f.write("\t\t\t\"dynn_" + cadet_dynasty + "\"\n")
                        f.write("\t\t}\n\n")
                    if section_line_count == 8:
                        dynasties = row[1].split()
                        f.write("\t\tdynasty_names = {\n")
                        for dynasty in dynasties:
                            f.write("\t\t\t\"dynn_" + dynasty + "\"\n")
                        f.write("\t\t}\n\n")
                    if section_line_count == 9:
                        f.write("\t\tdynasty_of_location_prefix = \"dynnp_" + row[1] + "\"\n\n")
                    if 10 <= section_line_count <= 15:
                        if row[1] != "x":
                            f.write("\t\t" + row[0] + " = " + row[1] + "\n")
                    if section_line_count == 16:
                        if row[1] != "x":
                            f.write("\t\tpatronym_prefix_male = \"dynnpat_pre_" + row[1] + "\"\n\n")
                    if section_line_count == 17:
                        if row[1] != "x":
                            f.write("\t\tpatronym_prefix_male_vowel = \"dynnpat_pre_vow_" + row[1] + "\"\n\n")
                    if section_line_count == 18:
                        if row[1] != "x":
                            f.write("\t\tpatronym_prefix_female = \"dynnpat_pre_" + row[1] + "\"\n\n")
                    if section_line_count == 19:
                        if row[1] != "x":
                            f.write("\t\tpatronym_prefix_female_vowel = \"dynnpat_pre_vow_" + row[1] + "\"\n\n")
                    if section_line_count == 20:
                        if row[1] != "x":
                            f.write("\t\tpatronym_suffix_male = \"dynnpat_suf_" + row[1] + "\"\n\n")
                    if section_line_count == 21:
                        if row[1] != "x":
                            f.write("\t\tpatronym_suffix_female = \"dynnpat_suf_" + row[1] + "\"\n\n")
                    if section_line_count == 22:
                        f.write("\t\talways_use_patronym = " + row[1] + "\n\n")
                    if 23 <= section_line_count <= 48:
                        if row[1] != "x":
                            ethnicities.append(row[0] + " = " + row[1])
                    if section_line_count == 49:
                        if row[1] != "x":
                            ethnicities.append(row[1] + " = " + row[0])
                        f.write("\t\tethnicities = {\n")
                        for ethnicity in ethnicities:
                            f.write("\t\t\t" + ethnicity + "\n")
                        f.write("\t\t}\n\n\t}\n\n")
                        section_line_count = -1
                        ethnicities = []
                    section_line_count = section_line_count + 1
            line_count = line_count + 1
        f.write("}")
    csv_file.close()


if __name__ == '__main__':
    culture_creation()

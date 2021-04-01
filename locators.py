def create_dummy_locators(starting_int, ending_int):
    f = open("building_locators.txt", "w")
    count = starting_int
    for i in range (ending_int - starting_int):
        f.write("\t\t{\n\t\t\tid=" + str(count) + "\n\t\t\tposition={ 4530.000000 0.000000 628.000000 "
                                                  "}\n\t\t\trotation={ "
                                              "-0.000000 -0.017503 -0.000000 -0.999847 }\n\t\t\tscale={ 1.000000 "
                                              "1.000000 1.000000 }\n\t\t}\n")
        count = count + 1


if __name__ == '__main__':
    create_dummy_locators(46, 2967)
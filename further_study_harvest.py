############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        # self.add_pairing()
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice cream")
    all_melon_types.append(yellow_watermelon) 


    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    # psuedocode
    # for each of the melons in melon_types, print the melon name
    # for each of the melon's pairings, print the pairing on separate lines

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")

# print_pairing_info(make_melon_types())


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_lookup = {}

    for melon in melon_types:
        melon_lookup[melon.code] = melon
    return melon_lookup

# make_melon_type_lookup(make_melon_types())

############
# Part 2   #
############

class Melon(MelonType):
    """A melon in a melon harvest."""

    # Fill in the rest

    # psuedo code: create a Melon class with the following:

        # an init method
            # self
            # melon type
            # shape rating
            # color rating
            # harvest field
            # harvester

        # an is_sellable method

    def __init__(self, melon_type, shape_rating, color_rating, harvest_field, harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvester = harvester
        #self.is_sellable = self.is_sellable(shape_rating, color_rating, harvest_field)

    def is_sellable(self, shape_rating, color_rating, harvest_field):
        return shape_rating > 5 and color_rating > 5 and harvest_field != 3

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    melon_list = []

    # psuedo code
    # open the file which gives us a file object with lines to loop through
    # loop through each line, strip whitespace, and split on spaces to create lists per line
    # assign a melon number based on the line number (FIGURE OUT HOW preferably without creating another dict)
    # 



    harvest_log = open('harvest_log.txt')

    melons_by_id = make_melon_type_lookup(melon_types)

    for idx, line in enumerate(harvest_log):
        line = line.split()
        melon_idx = Melon(melons_by_id[line[5]], line[1], line[3], line[11], line[8])
        print(melon_idx)
        melon_list.append(melon_idx)

    return melon_list    
    
        # print(idx, line)

    

    # melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    # melon_list.append(melon_1)
    harvest_log = open

    return melon_list

make_melons(make_melon_types())


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


    for melon in melons:
        sellable = '(CAN BE SOLD)' if melon.is_sellable else '(NOT SELLABLE)'
        print(f"Harvested by {melon.harvester} from Field {melon.harvest_field} {sellable}")


# get_sellability_report(make_melons(make_melon_types()))


# def open_file(filename):
#     '''Return list of each line of a text file

#     for example:
#         ['line 1 item 1', 'list 1 item 2'], ['line 2']'''

#     f = open(filename)
#     for line in f:
#         line = line.rstrip()
#         line = line.split()
#         print(line)

# open_file('harvest_log.txt')

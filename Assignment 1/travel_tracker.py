"""
CP1404 Assignment 1 - Travel Tracker 1.0
Name: Julie-Anne Roder
Date started:29/08/2020
GitHub URL: https://github.com/JulieRoder/Assignments/tree/master/Assignment%201
"""
HIGH_PRIORITY = 1
LOW_PRIORITY = 12
PRIORITY_LENGTH = 3
MENU = "Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit"
FILENAME = "places.csv"


def main():
    print("Travel Tracker 1.0 - by Julie-Anne Roder")
    places = get_places_data()
    print("{} places loaded from places.csv".format(len(places)))
    print(MENU)
    menu_options = ["L", "A", "M", "Q"]
    menu_choice = get_valid_menu_choice(menu_options)
    while menu_choice != "Q":
        if menu_choice == "L":
            display_places_list(places)
        elif menu_choice == "A":
            pass
        else:
            pass
        print(MENU)
        menu_choice = get_valid_menu_choice(menu_options)


def get_places_data():
    """Read data from places.csv file."""
    list_of_parts = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer
        list_of_parts.append(parts)
    input_file.close()
    return list_of_parts


def get_valid_menu_choice(menu):
    """Get a valid menu choice."""
    choice = input(">>> ").upper()
    while choice not in menu:
        print("Invalid menu choice")
        choice = input(">>> ").upper()
    return choice


def display_places_list(places):
    """Display list of places."""
    index = 0
    longest_place_name = get_longest_name(places, 0)
    longest_country_name = get_longest_name(places, 1)
    places.sort()
    for place in places:
        index += 1
        if place[3] == "n":
            print("*{}. {:<{}} in {:<{}} priority {:>{}}".format(index, place[0], longest_place_name, place[1],
                                                                 longest_country_name, place[2], PRIORITY_LENGTH))
        else:
            print(" {}. {:<{}} in {:<{}} priority {:>{}}".format(index, place[0], longest_place_name, place[1],
                                                                 longest_country_name, place[2], PRIORITY_LENGTH))


def get_longest_name(list_file, index):
    """Get length of longest name."""
    longest_name = 0
    for parts in list_file:
        if len(parts[index]) > longest_name:
            longest_name = len(parts[index])
    return longest_name


if __name__ == '__main__':
    main()

"""
CP1404 Assignment 1 - Travel Tracker 1.0
Name: Julie-Anne Roder
Date started:29/08/2020
GitHub URL: https://github.com/JulieRoder/Assignments/tree/master/Assignment%201
"""
from operator import itemgetter
FILENAME = "places.csv"
MENU = "Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit"
SENTINEL = 1
VISITED_INDEX = 3
PRIORITY_INDEX = 2
COUNTRY_INDEX = 1
PLACE_NAME_INDEX = 0
PRIORITY_LENGTH = 3


def main():
    print("Travel Tracker 1.0 - by Julie-Anne Roder")
    places = get_places_data()
    places.sort(key=itemgetter(VISITED_INDEX, PRIORITY_INDEX))
    print("{} places loaded from places.csv".format(len(places)))
    print(MENU)
    menu_options = ["L", "A", "M", "Q"]
    menu_choice = get_valid_menu_choice(menu_options)
    while menu_choice != "Q":
        if menu_choice == "L":
            display_places_list(places)
        elif menu_choice == "A":
            place_details = collect_place_details()
            places.append(place_details)
            places.sort(key=itemgetter(VISITED_INDEX, PRIORITY_INDEX))
        else:
            display_places_list(places)

            places.sort(key=itemgetter(VISITED_INDEX, PRIORITY_INDEX))
            pass
        print(MENU)
        menu_choice = get_valid_menu_choice(menu_options)


def get_places_data():
    """Read data from places.csv file."""
    list_of_parts = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[PRIORITY_INDEX] = int(parts[PRIORITY_INDEX])
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
    longest_place_name = get_longest_name(places, PLACE_NAME_INDEX)
    longest_country_name = get_longest_name(places, COUNTRY_INDEX)
    for place in places:
        index += 1
        visit_marker = "*" if place[VISITED_INDEX] == "n" else " "
        print("{}{}. {:<{}} in {:<{}} priority {:>{}}".format(visit_marker, index, place[PLACE_NAME_INDEX],
                                                              longest_place_name, place[COUNTRY_INDEX],
                                                              longest_country_name, place[PRIORITY_INDEX],
                                                              PRIORITY_LENGTH))


def get_longest_name(list_file, index):
    """Get length of longest name."""
    longest_name = 0
    for parts in list_file:
        if len(parts[index]) > longest_name:
            longest_name = len(parts[index])
    return longest_name


def get_valid_string(prompt):
    """Get a valid string."""
    string = input(prompt).title()
    while string == "":
        print("Input can not be blank")
        string = input(prompt).title()
    return string


def get_valid_number(prompt):
    """Get a valid number."""
    finished = False
    while not finished:
        try:
            number = int(input(prompt))
            if number < SENTINEL:
                print("number must be > 0")
            else:
                finished = True
        except ValueError:  # if user enters letter instead of number.
            print("Invalid input; enter a valid number")
    return number


def collect_place_details():
    """Collect the place details."""
    place_details = []
    place_name = get_valid_string("Name: ")
    place_details.append(place_name)
    country_name = get_valid_string("Country: ")
    place_details.append(country_name)
    priority_value = get_valid_number("Priority: ")
    place_details.append(priority_value)
    place_details.append("n")
    return place_details


if __name__ == '__main__':
    main()

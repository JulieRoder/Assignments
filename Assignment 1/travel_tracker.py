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
STARTING_VALUE = 0
VISITED_INDEX = 3
PRIORITY_INDEX = 2
COUNTRY_INDEX = 1
PLACE_NAME_INDEX = 0
PRIORITY_LENGTH = 3
UNVISITED_MARKER = "n"
VISITED_MARKER = "v"


def main():
    """Track the travel plans of the user."""
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
            visited_count = count_visited_places(places)
            if visited_count == len(places):
                print("No unvisited places")
            else:
                display_places_list(places)
                mark_place_as_visited(places)
                places.sort(key=itemgetter(VISITED_INDEX, PRIORITY_INDEX))
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
    index = STARTING_VALUE
    longest_place_name = get_longest_name(places, PLACE_NAME_INDEX)
    longest_country_name = get_longest_name(places, COUNTRY_INDEX)
    visited_count = count_visited_places(places)
    for place in places:
        index += 1
        unvisited_marker = "*" if place[VISITED_INDEX] == UNVISITED_MARKER else " "
        print("{}{}. {:<{}} in {:<{}} priority {:>{}}".format(unvisited_marker, index, place[PLACE_NAME_INDEX],
                                                              longest_place_name, place[COUNTRY_INDEX],
                                                              longest_country_name, place[PRIORITY_INDEX],
                                                              PRIORITY_LENGTH))
        print("{} places. You still want to visit {} places.".format(len(places), len(places) - visited_count))


def get_longest_name(list_file, index):
    """Get length of longest name."""
    longest_name = STARTING_VALUE
    for parts in list_file:
        if len(parts[index]) > longest_name:
            longest_name = len(parts[index])
    return longest_name


def count_visited_places(places):
    """Count the number of places visited."""
    visited_count = STARTING_VALUE
    for place in places:
        if place[VISITED_INDEX] == VISITED_MARKER:
            visited_count += 1
    return visited_count


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
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


def collect_place_details():
    """Collect the place details."""
    place_name = get_valid_string("Name: ")
    country_name = get_valid_string("Country: ")
    priority_value = get_valid_number("Priority: ")
    place_details = [place_name, country_name, priority_value, UNVISITED_MARKER]
    print("{} in {} (priority {}) added to Travel Tracker".format(place_name, country_name, priority_value))
    return place_details


def mark_place_as_visited(places):
    """Mark a place as visited."""
    place_visited = get_valid_number("Enter the number of a place to mark as visited\n>>> ")
    while place_visited > len(places):
        print("Invalid place number")
        place_visited = get_valid_number("Enter the number of a place to mark as visited\n>>> ")
    if places[place_visited - 1][VISITED_INDEX] == VISITED_MARKER:
        print("That place is already visited")
    else:
        places[place_visited - 1][VISITED_INDEX] = VISITED_MARKER
        print("{} in {} visited".format(places[place_visited - 1][PLACE_NAME_INDEX],
                                        places[place_visited - 1][COUNTRY_INDEX]))


if __name__ == '__main__':
    main()

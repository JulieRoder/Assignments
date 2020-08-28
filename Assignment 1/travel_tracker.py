"""
CP1404 Assignment 1 - Travel Tracker 1.0
Name: Julie-Anne Roder
Date started:29/08/2020
GitHub URL: https://github.com/JulieRoder/Assignments/tree/master/Assignment%201
"""
HIGH_PRIORITY = 1
LOW_PRIORITY = 12
MENU = "Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit"
FILENAME = "places.csv"


def main():
    print("Travel Tracker 1.0 - by Julie-Anne Roder")
    places = get_places_data()
    print("{} places loaded from places.csv".format(len(places)))


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


if __name__ == '__main__':
    main()

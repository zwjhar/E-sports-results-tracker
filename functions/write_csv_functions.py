import csv

from functions.clean_csv_data import clean_data
from functions.duplicate_csv_data import duplicate_csv_data


def write_to_csv(filename, *data):
    """
    Function that appends to CSV based on which filename is carried through. This is for when new data is added.
    """

    with open(f"{filename}.csv", mode="a", newline="") as file:  # Open the CSV in append mode.
        writer = csv.writer(file)
        if filename == "game_names":  # If filename is game_names do this.
            writer.writerow([data[0]])  # Append the new entry to the first column.

        elif filename == "teams":  # If filename is teams do this.
            writer.writerow([data[0], 0])  # Append the team name in column 1 and set the team score as 0.

        else:  # This covers the match_data csv.
            writer.writerow(data)  # Append all the stored data (list) to a new row.

    # This functions removes duplicates to ensure data validation is carried out
    # without needing to throw lots of errors.
    clean_data(filename)

    # Duplicate data to ensure data security.
    duplicate_csv_data(filename)

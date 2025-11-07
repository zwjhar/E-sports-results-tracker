import csv
import os

from functions.duplicate_csv_data import duplicate_csv_data


def file_not_found_at_all(filename):
    """
    This function accounts for a CSV file not being found - it either renames a duplicate (if available) or creates a
    new file with the header names set out below.
    """

    data = [[]]

    # Define headers based on the filename that is passed through.
    if filename == "teams":
        data = [["team name", "team scores"]]

    elif filename == "game_names":
        data = [["game name"]]

    elif filename == "match_data":
        data = [["date", "team 1", "team 2", "game played", "winning team"]]

    # This ensures the new csv file is stored in the right (parent) directory. Without this it stores in functions
    # and can't be accessed.
    csv_file_path = os.path.abspath(__file__ + f"/../../{filename}.csv")

    # Create and write the new CSV with the above headers.
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


def file_not_found_rename_duplicate(filename):

    try:  # to rename the duplicate if one exists.
        os.rename(f"copy_of_{filename}.csv", f"{filename}.csv")

    except FileNotFoundError:  # create a new CSV using the function above.
        file_not_found_at_all(filename)

    # duplicate the new CSV so there is a backup.
    duplicate_csv_data(filename)

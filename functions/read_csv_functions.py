import csv

from functions.file_not_found import (file_not_found_rename_duplicate)

from datetime import datetime


def read_csv(filename, sorted_data=False):
    try:  # Opening the csv first, if it exists.
        with open(f"{filename}.csv", mode="r") as file:
            reader = csv.reader(file)
            if sorted_data:  # If data needs to be sorted, the logic follows this.
                headers = next(reader)
                if filename == "by_game_scores" or filename == "teams":  # Sorting for scores by game function.
                    rows = sorted(reader, key=lambda row: int(row[1]), reverse=True)
                else:
                    # Sort by date in descending order for match_data.
                    rows = sorted(
                        reader,
                        key=lambda row: datetime.strptime(row[0], "%d-%m-%Y"),
                        reverse=True
                        )
                return headers, rows  # Return data to be used.

            else:  # Non-sorted data.
                headers = next(reader)
                rows = list(reader)
                return headers, rows

    except FileNotFoundError:  # If a file isn't found.
        file_not_found_rename_duplicate(filename)


def read_csv_column(filename, column_index=0):
    """
    This function has been developed so that a Combobox can be used to input results. This takes away the issue of
    incorrect team or game names being inputted, thus reducing the risk of the app breaking.

    The column_index has been set as 1 on purpose as most names are contained in column 1. This can be changed, though,
    when the function is called if required.
    """
    # Save the retrieved data in a list that the combobox can use.
    column_data = []
    try:  # this first if the file exists.
        headers, rows = read_csv(filename)  # Read in the CSV to get the data.
        for row in rows:
            if row:
                column_data.append(row[column_index])  # Save column name to list above to be used.
        return column_data  # Return column data to be displayed.

    # This accounts for the file not existing and will show an error message instead.
    except FileNotFoundError:
        if filename == "teams":
            return ["No teams found."]  # Error catching based on filename.

        if filename == "game_names":
            return ["No games found."]  # Error catching based on filename.

import csv

from functions.display_csv_data import display_csv_data
from functions.read_csv_functions import read_csv


def tab_switcher_data_gather(parent, current_tab):
    """
    # This function operates the scores by game tab switcher.

    """

    game_scores_data = {}  # Empty dict to store team name and their score

    # Read in the data, unsorted.
    headers, rows = read_csv("match_data", False)

    # Iterate through the CSV, row by row.
    for row in rows:
        game_names = row[3]  # Set where game_names will be found.
        winning_team = row[4]  # Set where winning_team can be found.

        # Check that the current tab name matches the game name.
        if game_names == current_tab:
            # Check if winning team is in the dictionary, if yes up their score by 1.
            if winning_team in game_scores_data.keys():
                game_scores_data[winning_team] += 1

            # If not, set their score as 1.
            else:
                game_scores_data[winning_team] = 1

    # Define the header for a new CSV file which will store game data.
    header_data = [["team name", "scores"]]

    # File name for the new CSV.
    filename = "by_game_scores"

    # Open a new CSV in write mode.
    with open(f"{filename}.csv", mode="w", newline="") as file:
        writer = csv.writer(file)  # Create a writer.
        writer.writerows(header_data)  # Write the header row.
        # Write team names and their score to be displayed using a function.
        for team_name, score in game_scores_data.items():
            writer.writerow([team_name, score])

    # Display the new CSV data in the scrollable frame.
    display_csv_data(parent, filename, False, True, None)

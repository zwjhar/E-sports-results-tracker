import csv
import time
from datetime import datetime

import customtkinter as ctk
from tkcalendar import DateEntry

from functions.duplicate_csv_data import duplicate_csv_data
from functions.read_csv_functions import read_csv_column, read_csv
from functions.write_csv_functions import write_to_csv


# region Add new match record and add team score function
def add_new_match_record(filename, parent, date_entry, team_1_entry, team_2_entry, game, winner, error, submit):

    # region Add new match data to match data CSV.

    # Retrieve entries from combo boxes.
    date = return_and_convert_date_entry(date_entry)
    team_1_name = team_1_entry.get()
    team_2_name = team_2_entry.get()
    game_name = game.get()
    winning_team = winner.get()

    # Error checking to ensure winning team is a valid choice.
    if winning_team != team_1_name and winning_team != team_2_name:  # 'and' ensures it is checked against both entries.
        error.configure(text=f"Winning team must be {team_1_name} or {team_2_name}.")  # Error message.
        submit.place(rely=0.85)  # Move submit button down to make way for error message.
        return  # Return back to start of function.

    # Store in  a list to make appending to existing csv easier.
    data = [date, team_1_name, team_2_name, game_name, winning_team]

    # Function that appends inputted data to CSV.
    write_to_csv(filename, *data)

    # endregion

    # region Allocate team score to winning team

    # Read CSV to allocate point to winning team's score.
    headers, rows = read_csv("teams", False)

    # Iteration to locate winning team and increment team score.
    for team_name in rows:
        if team_name[0] == winning_team:
            team_name[1] = str(int(team_name[1]) + 1)  # Had to convert because data is held in CSV as a string.

    # Write newly incremented team score data to CSV.
    with open("teams.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

    # Duplicate CSV to ensure data is safe and backed up.
    duplicate_csv_data("teams")

    # endregion

    time.sleep(3)
    parent.destroy()

# endregion

# region Convert to UK date function.


def return_and_convert_date_entry(entry):
    """
    DateEntry is a US formatted date. This function converts it to Uk standard.

    """

    # Get current entry.
    us_date = entry.get_date()

    # Convert to UK date so that it sticks to the set out format in the CSV.
    uk_date = datetime.strptime(f"{us_date}", "%Y-%m-%d").strftime("%d-%m-%Y")

    # Return date to ensure it can be used for appending to the CSV.
    return uk_date

# endregion

# region Function to create CTk Top Level to add new match


def spawn_add_match(filename, parent):

    # region Top Level configurations

    add_match_top = ctk.CTkToplevel(parent)
    add_match_top.title("Add new match | E-SPORTS Results App")
    add_match_top.geometry("300x400")
    add_match_top.resizable(False, False)

    # endregion

    # region Top Level widgets

    error_label = ctk.CTkLabel(
        add_match_top,
        text="",
        text_color="red",
        font=("Inter", 10)
    )

    error_label.place(
        relx=0.5,
        rely=0.81,
        anchor="center"
    )

    exit_button = ctk.CTkButton(
        add_match_top,
        text="Go back",
        width=50,
        corner_radius=8,
        fg_color="#FFFFFF",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        command=lambda: add_match_top.destroy()
    )

    exit_button.place(
        relx=0.1,
        rely=0.05,
        anchor="nw"
    )

    date_entry_label = ctk.CTkLabel(
        add_match_top,
        text="Date:",
        font=("Inter", 12)
    )

    date_entry_label.place(
        relx=0.15,
        rely=0.2,
        anchor="nw"
    )

    date_entry = DateEntry(
        add_match_top,
        font=("Inter", 16),
        width=20,
        height=4,
        date_pattern="dd-mm-yyyy",
    )

    date_entry.place(
        relx=0.26,
        rely=0.2175,
        anchor="nw"
    )

    team_1_label = ctk.CTkLabel(
        add_match_top,
        text="Team 1:",
        font=("Inter", 12)
    )

    team_1_label.place(
        relx=0.10,
        rely=0.325,
        anchor="nw"
    )

    team_1_choice = ctk.CTkComboBox(
        add_match_top,
        values=read_csv_column("teams"),
        width=150,
        border_width=0
    )

    team_1_choice.place(
        relx=0.26,
        rely=0.325,
        anchor="nw"
    )

    team_2_label = ctk.CTkLabel(
        add_match_top,
        text="Team 2:",
        font=("Inter", 12)
    )

    team_2_label.place(
        relx=0.1,
        rely=0.45,
        anchor="nw"
    )

    team_2_choice = ctk.CTkComboBox(
        add_match_top,
        values=read_csv_column("teams"),
        width=150,
        border_width=0
    )

    team_2_choice.place(
        relx=0.26,
        rely=0.45,
        anchor="nw"
    )

    game_label = ctk.CTkLabel(
        add_match_top,
        text="Game:",
        font=("Inter", 12)
    )

    game_label.place(
        relx=0.125,
        rely=0.575,
        anchor="nw"
    )

    game_choice = ctk.CTkComboBox(
        add_match_top,
        values=read_csv_column("game_names"),
        width=150,
        border_width=0
    )

    game_choice.place(
        relx=0.26,
        rely=0.575,
        anchor="nw"
    )

    winning_team_label = ctk.CTkLabel(
        add_match_top,
        text="Winner:",
        font=("Inter", 12)
    )

    winning_team_label.place(
        relx=0.1,
        rely=0.7,
        anchor="nw"
    )

    winning_team_choice = ctk.CTkComboBox(
        add_match_top,
        values=read_csv_column("teams"),
        width=150,
        border_width=0
    )

    winning_team_choice.place(
        relx=0.26,
        rely=0.7,
        anchor="nw"
    )

    add_new_button = ctk.CTkButton(
        add_match_top,
        text="Add a new match",
        width=250,
        height=30,
        corner_radius=8,
        fg_color="#FFFFFF",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        command=lambda: add_new_match_record(
            filename,
            add_match_top,
            date_entry,
            team_1_choice,
            team_2_choice,
            game_choice,
            winning_team_choice,
            error_label,
            add_new_button
        )
    )

    add_new_button.place(
        relx=0.075,
        rely=0.825,
        anchor="nw"
    )

    # endregion

# endregion

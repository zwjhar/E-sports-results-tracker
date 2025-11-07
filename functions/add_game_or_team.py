import customtkinter as ctk

from functions.activate_placeholder import re_activate_placeholder
from functions.duplicate_csv_data import duplicate_csv_data
from functions.retrieve_and_format_entries import retrieve_entry, format_to_title_case
from functions.write_csv_functions import write_to_csv
from functions.read_csv_functions import read_csv

# region Function to add new team or game to CSV.


def add_game_or_team(filename, entry, top, error_label, btn):
    while True:  # Error catching won't work unless it is in a while true loop.

        # Set text variables to make this function modular, based on filename.
        if filename == "game_names":
            text_variable = "game"

        else:
            text_variable = "team"

        headers, rows = read_csv(filename)  # Read in CSV data.

        new_entry = retrieve_entry(entry)  # Retrieve entry to be saved from the Top Level.

        formatted_name = format_to_title_case(new_entry)  # Correctly format the entry for storing.

        # Error catching - nothing entered.
        if len(formatted_name) == 0:
            error_label.configure(text=f"No {text_variable} entered. Please try again.", text_color="red", pady=5)
            btn.place(rely=0.65)
            re_activate_placeholder(entry)
            break

        # Error catching - search for a duplicate.
        duplicate_found = False
        for row in rows:
            if len(row) > 0 and row[0].strip() == formatted_name:
                duplicate_found = True
                break

        if duplicate_found:
            error_label.configure(text="Duplicate entry. Please try again.", text_color="red", pady=5)
            re_activate_placeholder(entry)

            btn.place(rely=0.65)
            break

        write_to_csv(filename, formatted_name)  # Write new entry to CSV.

        top.after(2000, duplicate_csv_data(filename))  # 2000ms = 2 seconds.

        top.after(2000, top.destroy())

        break

# endregion

# region Function to spawn toplevel to add new team or game


def spawn_add_game_or_team(parent, filename):

    # region Toplevel configurations
    top = ctk.CTkToplevel(parent)
    if filename == "game_names":  # Condition to ensure the right names are displayed based on use.
        top.title("Add a new game | E-SPORTS Results App")
        name_variable = "game's"
    else:
        top.title("Add a new team | E-SPORTS Results App")
        name_variable = "team"
    top.geometry("300x300")
    top.resizable(False, False)

    # endregion

    # region Toplevel widgets

    error_label = ctk.CTkLabel(
        top,
        text="",
        text_color="red",
        font=("Inter", 10)
    )

    error_label.place(
        relx=0.5,
        rely=0.55,
        anchor="center"
    )

    entry = ctk.CTkEntry(
        top,
        placeholder_text=f"Please enter the {name_variable} name...",
        font=("Inter", 12),
        width=250,
        border_width=0
        )

    entry.place(
        relx=0.5,
        rely=0.45,
        anchor="center"
    )

    exit_button = ctk.CTkButton(
        top,
        text="Go back",
        width=50,
        corner_radius=8,
        fg_color="#FFFFFF",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        command=lambda: top.destroy()
    )

    exit_button.place(
        relx=0.1,
        rely=0.1,
        anchor="nw"
    )

    btn = ctk.CTkButton(
        top,
        text="",
        width=250,
        height=30,
        corner_radius=8,
        fg_color="#FFFFFF",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        command=lambda: add_game_or_team(filename, entry, top, error_label, btn)
    )

    # Accounts for the different button texts needed based on filename.
    if filename == "game_names":
        btn.configure(text="Add new game")

    else:
        btn.configure(text="Add new team")

    btn.place(
        relx=0.5,
        rely=0.6,
        anchor="center",
    )

    # endregion

# endregion

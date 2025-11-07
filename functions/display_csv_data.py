import csv

import customtkinter as ctk

from functions.make_ctk_image import make_ctk_image
from functions.read_csv_functions import read_csv

# region Create CTK delete 'x' icon.
# This creates the x icon for the delete row button.
delete_icon = make_ctk_image("x.png", (18, 18))

# endregion

# region Function that creates a top level to confirm deletion.


def top_delete_confirmation_button(parent, filename, data_id, sorted_data):

    """
    Create a top level which asks for user confirmation to delete data.

    """

    # region Top level configurations
    confirmation_top = ctk.CTkToplevel(parent)
    confirmation_top.title("Confirm deletion | E-SPORTS Results App")
    confirmation_top.geometry("450x200")
    confirmation_top.resizable(False, False)
    # endregion

    # region Top level widgets
    confirmation_label = ctk.CTkLabel(
        confirmation_top,
        text="Are you sure you want to delete this record?",
        font=("Inter", 14)
    )

    confirmation_label.place(
        relx=0.175,
        rely=0.35,
        anchor="w"
    )

    confirmation_yes_button = ctk.CTkButton(
        confirmation_top,
        text="Yes",
        width=50,
        corner_radius=8,
        fg_color="#FFFFFF",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        command=lambda: delete_row_of_data(confirmation_top, filename, data_id, sorted_data)
    )

    confirmation_yes_button.place(
        relx=0.32,
        rely=0.55,
        anchor="w"
    )

    confirmation_no_button = ctk.CTkButton(
        confirmation_top,
        text="No",
        width=50,
        corner_radius=8,
        fg_color="#FFFFFF",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        command=lambda: confirmation_top.destroy()
    )

    confirmation_no_button.place(
        relx=0.52,
        rely=0.55,
        anchor="w"
    )

    # endregion

# endregion

# region Function to delete row of data.


def delete_row_of_data(parent, filename, data_id, sorted_data):
    """
    Modular function that handles deleting a row - team, game name or match data. Multi-use.
    """

    # Ensure the confirmation top level is destroyed when the yes button is pressed.
    parent.destroy()

    # Get data from CSV to delete - sorted inc to make sure it is formatted based on use case.
    if sorted_data:
        headers, rows = read_csv(filename, True)

    else:
        headers, rows = read_csv(filename)

    # Deletion of the corresponding row - id has carried through.
    rows.pop(data_id)

    # Re-write the CSV with the headers first (not changed) and the rows (changed).
    # This approach has been taken to ensure the headers get carried over correctly otherwise they'll be lost...
    with open(f"{filename}.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

# endregion

# region Function that displays data. based on what is passed through.


def display_csv_data(parent, filename, admin=False, sorted_data=True, match_display_limit=None):

    # region Get data from CSV.

    # Get CSV data based on data passed through in original function call.
    headers, rows = read_csv(filename, sorted_data)

    # endregion

    # region Data display limit.

    # Limit how many rows are shown based on the requirement to show 5 in the user side of the app.
    rows = rows[:match_display_limit]

    # endregion

    # region Title display (top of table).

    # Loop which iterates over header data to find the columns and titles.
    # The statement below then creates a label for each item found in the list and displays using grid.
    for column, title in enumerate(headers):
        display_table_title_label = ctk.CTkLabel(
            parent,
            text=title.capitalize(),  # Capitalise title to make it look presentable.
            font=("Inter", 12, "bold"),
            fg_color="#EAEAEA",
            padx=15
        )

        display_table_title_label.grid(
            row=0,
            column=column,
            padx=10,
            pady=5,
            sticky="nsew"
            )

    # endregion

    # region Data (rows) display.

    # This iterates over the list to get the data and its correct placement using row_id.
    for row_id, row in enumerate(rows, start=1):  # start=1 ensures that the titles are displayed.
        for column_id, data in enumerate(row):  # This iterates over
            data_label = ctk.CTkLabel(
                parent,
                text=data,
                font=("Inter", 12)
            )

            data_label.grid(
                row=row_id,
                column=column_id,
                padx=10,
                pady=5,
                sticky="nsew"
            )

        # This ensures we can use one function to display and displays a delete button when in admin mode.
        if admin:
            delete_button = ctk.CTkButton(
                parent,
                width=5,
                fg_color="#FFFFFF",
                hover_color="#E6E6E6",
                image=delete_icon,
                text="",
                # (row_id - 1) ensures we are selecting the right entry to delete as start=1 above.
                command=lambda delete_id=(row_id - 1): top_delete_confirmation_button(
                    parent,
                    filename,
                    delete_id,
                    sorted_data
                )
            )

            delete_button.grid(
                row=row_id,
                column=len(headers),
                padx=10,
                pady=5,
                sticky="nsew"
            )

    for column in range(len(headers) + 1):
        parent.grid_columnconfigure(
            column,
            weight=1
        )

    # endregion

# endregion

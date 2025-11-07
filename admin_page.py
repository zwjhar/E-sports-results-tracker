import customtkinter as ctk

from functions.add_game_or_team import spawn_add_game_or_team
from functions.add_match import spawn_add_match
from functions.display_csv_data import display_csv_data
from functions.make_ctk_image import make_ctk_image


def create_admin_page(parent):
    """
    Function that is called and creates the user page - including its children.
    """

    # region Admin page functions

    # Function that accounts for the teams button press.
    def switch_to_teams(previous_data_frame):
        # region Menu button configurations.

        # Match results button re-configure to change to its non-pressed state and giving a command to use.
        match_results_button.configure(
            fg_color="#FFFFFF",
            command=lambda: create_admin_page(parent)
        )

        # Change the teams button colour now it has been pressed and removing the command as that frame is shown.
        teams_button.configure(
            fg_color="#F7F7F7",
            command=None
        )

        # Change the games button to ensure the colour is right and that the previous frame is carried through
        # so it can be destroyed when switching.
        games_button.configure(
            fg_color="#FFFFFF",
            command=lambda: switch_to_games(team_data)
        )
        # endregion

        # region Display title configurations.
        main_display_title.configure(
            text="Teams"
        )

        main_display_subtitle.configure(
            text="Showing all registered teams"
        )

        # endregion

        # region Button to add a new team.

        add_new_button.configure(
            text="Add a new team",
            command=lambda: spawn_add_game_or_team(information_display_frame, "teams")
        )

        # endregion

        # region Forget previous frame
        # This needs to be done to be able to display the new frame. Scrollable frame can't use .destroy().
        previous_data_frame.pack_forget()
        # endregion

        # region ScrollableFrame to display team data

        # Scrollable frame has been used to ensure no data is missing.
        team_data = ctk.CTkScrollableFrame(
            information_display_frame,
            width=350,
            height=375
        )

        team_data.pack(
            pady=(5, 20),
            padx=50,
            anchor="w"
        )

        # endregion

        # region Function call to display team data.

        # Call the function that displays the data.
        display_csv_data(team_data, "teams", True, True)

        # endregion

    # Function that accounts for the game names button being pressed.
    def switch_to_games(previous_data_frame):

        # region Menu button configurations.
        #  Match results button re-configure to change to its non-pressed state and giving a command to use.
        match_results_button.configure(
            fg_color="#FFFFFF",
            command=lambda: create_admin_page(parent)
        )

        # Change the teams button and ensuring it has a command so it can be used again.
        teams_button.configure(
            fg_color="#FFFFFF",
            command=lambda: switch_to_teams(game_data)
        )

        # Remove command here and change colour state so UX knows it has been selected.
        games_button.configure(
            fg_color="#F7F7F7",
            command=None
        )

        # endregion

        # region Title configurations
        # This is to ensure the right text is displayed in the titles so UX knows the page.
        main_display_title.configure(
            text="Games"
        )

        main_display_subtitle.configure(
            text="Showing all registered games"
        )
        # endregion

        # region Button to add a new game to the system.

        add_new_button.configure(
            text="Add a new game",
            command=lambda: spawn_add_game_or_team(information_display_frame, "game_names")
        )

        # endregion

        # region Forget previous frame.

        # Scrollable frames can't be destroyed so have to use .pack_forget().
        previous_data_frame.pack_forget()

        # endregion

        # region ScrollableFrame to display game data

        # A scrollable frame has been used to ensure all data can be fitted.
        game_data = ctk.CTkScrollableFrame(
            information_display_frame,
            width=200,
            height=375
        )

        game_data.pack(
            pady=(5, 20),
            padx=50,
            anchor="w"
        )

        # endregion

        # region Function call to display game data

        # Modular command that has been set to show game data based on what is passed through.
        display_csv_data(game_data, "game_names", True, False)

        # endregion

    # endregion

    # region Main admin page frame configuration.
    admin_page_frame = ctk.CTkFrame(
        parent,
        width=1040,
        height=560,
        corner_radius=0,
        border_width=0,
    )

    admin_page_frame.grid(
        row=0,
        column=0,
        sticky="nsew",
        columnspan=2
    )
    # endregion

    # region Side bar frame configuration.
    admin_side_bar_frame = ctk.CTkFrame(
        admin_page_frame,
        width=225,
        height=560,
        corner_radius=0,
        border_width=0,
        fg_color="#FFFFFF"
    )

    admin_side_bar_frame.grid(
        row=0,
        column=0,
        sticky="ns"
    )

    # endregion

    # region Create CTk friendly icons for buttons
    settings_icon = make_ctk_image("settings.png", (18, 18))
    people_icon = make_ctk_image("people.png", (18, 18))
    game_icon = make_ctk_image("game.png", (18, 18))
    x_icon = make_ctk_image("x.png", (18, 18))
    plus_icon = make_ctk_image("plus.png", (18, 18))
    # endregion

    # region Admin menu frame configuration
    admin_menu_frame = ctk.CTkFrame(
        admin_side_bar_frame,
        corner_radius=0,
        border_width=0,
        fg_color="#FFFFFF",
        bg_color="#FFFFFF"
    )

    admin_menu_frame.grid(
        row=0,
        column=0,
        sticky="ne"
    )
    # endregion

    # region Admin menu frame widgets
    admin_title_label = ctk.CTkLabel(
        admin_menu_frame,
        text="E-SPORTS RESULTS TRACKER",
        font=("Inter", 16, "bold"),
        fg_color="#FFFFFF"
    )

    admin_title_label.pack(
        pady=(50, 0),
        padx=25,
        anchor="center"
    )

    admin_text_label = ctk.CTkLabel(
        admin_menu_frame,
        text="Administrator panel",
        font=("Inter", 14, "bold")
    )

    admin_text_label.pack(
        pady=(20, 0),
        padx=25,
        anchor="w"
    )

    match_results_button = ctk.CTkButton(
        admin_menu_frame,
        text="Match results",
        width=200,
        height=30,
        corner_radius=8,
        fg_color="#F7F7F7",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        image=settings_icon,
        compound="left",
        anchor="w"
    )

    match_results_button.pack(
        pady=(15, 0),
        padx=15,
        anchor="w"
    )

    teams_button = ctk.CTkButton(
        admin_menu_frame,
        text="Teams",
        width=200,
        height=30,
        corner_radius=8,
        fg_color="#FFFFFF",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        image=people_icon,
        compound="left",
        anchor="w",
        command=lambda: switch_to_teams(match_data)
    )

    teams_button.pack(
        pady=(15, 0),
        padx=15,
        anchor="w"
    )

    games_button = ctk.CTkButton(
        admin_menu_frame,
        text="Games",
        width=200,
        height=30,
        corner_radius=8,
        fg_color="#FFFFFF",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        image=game_icon,
        compound="left",
        anchor="w",
        command=lambda: switch_to_games(match_data)
    )

    games_button.pack(
        pady=(15, 0),
        padx=15,
        anchor="w"
    )

    line = ctk.CTkCanvas(
        admin_menu_frame,
        bg="#FFFFFF",
        bd=0,
        highlightthickness=0,
        height=40
    )

    line.pack(
        pady=(20, 0),
        padx=50,
        anchor="w"
    )

    line.create_line(0, 25, 350, 25, fill="#E6E6E6")

    return_to_login_button = ctk.CTkButton(
        admin_menu_frame,
        text="Exit the application",
        width=200,
        height=30,
        corner_radius=8,
        fg_color="#FFFFFF",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        image=x_icon,
        compound="left",
        anchor="w",
        command=lambda: exit()
    )

    return_to_login_button.pack(
        pady=(220, 20),
        padx=15,
        anchor="w"
    )
    # endregion

    # region Main display frame configurations
    main_display_frame = ctk.CTkFrame(
        admin_page_frame,
        width=815,
        height=560,
        fg_color="#ECECEC",
        corner_radius=0,
        border_width=0
    )

    main_display_frame.grid(
        row=0,
        column=1,
        sticky="nsew",
        columnspan=2
    )
    # endregion

    # region Information display frame configurations
    information_display_frame = ctk.CTkFrame(
        main_display_frame,
        corner_radius=0,
        border_width=0,
        fg_color="#ECECEC",
        bg_color="#ECECEC"
    )

    information_display_frame.grid(
        row=0,
        column=0,
        sticky="nsew"
    )
    # endregion

    # region Information display frame widgets

    main_display_title = ctk.CTkLabel(
        information_display_frame,
        text="Match results",
        font=("Inter", 16, "bold")
    )

    main_display_title.pack(
        pady=(50, 0),
        padx=(50, 0),
        anchor="w"
    )

    main_display_subtitle = ctk.CTkLabel(
        information_display_frame,
        text="Showing all results recorded",
        font=("Inter", 11),
        text_color="#454545"
    )

    main_display_subtitle.pack(
        padx=50,
        anchor="w"
    )

    # endregion

    # region Button to add a new match.

    add_new_button = ctk.CTkButton(
        information_display_frame,
        text="Add a new match",
        width=150,
        height=30,
        corner_radius=8,
        fg_color="#FFFFFF",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        image=plus_icon,
        compound="left",
        anchor="w",
        command=lambda: spawn_add_match("match_data", information_display_frame)
    )

    add_new_button.pack(
        pady=0,
        padx=(570, 30),
        anchor="w"
    )

    # endregion

    # region Match data frame configurations

    # Frame that holds the matches data.
    match_data = ctk.CTkScrollableFrame(
        information_display_frame,
        width=650,
        height=375
    )

    match_data.pack(
        pady=(5, 20),
        padx=50,
        anchor="w"
    )

    # endregion

    # region Function to create match data frame widgets
    # Function call to display match data based on the information that is passed through.
    display_csv_data(match_data, "match_data", True)

    # endregion

    # region Admin page frame configurations
    admin_page_frame.grid_rowconfigure(0, weight=1)
    admin_page_frame.grid_columnconfigure(0, weight=1)
    admin_page_frame.grid_columnconfigure(1, weight=1)
    # endregion

    # Return of the overall frame to ensure it displays correctly when called.
    return admin_page_frame

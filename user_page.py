import customtkinter as ctk

from functions.by_game_scores_display import tab_switcher_data_gather
from functions.display_csv_data import display_csv_data
from functions.make_ctk_image import make_ctk_image
from functions.read_csv_functions import read_csv_column


def create_user_page(parent):
    """
    Function that is called and creates the user page - including its children and their respective widgets.

    Return overall frame for proper displaying.
    """

    # region User page functions

    def switch_to_scoreboard(previous_data_frame):
        """
        Function that accounts for the scoreboard button press.
        """

        # region Menu button configurations.

        # Recent results button re-configure to change to its non-pressed state and giving a command to use.
        recent_match_result_button.configure(
            fg_color="#FFFFFF",
            command=lambda: create_user_page(parent)
        )

        # Change the scoreboard button colour now it has been pressed and removing the command as that frame is shown.
        scoreboard_button.configure(
            fg_color="#F7F7F7",
            command=None
        )

        # Change the scores by game button to ensure the colour is right and that the previous frame is carried through
        # so it can be destroyed when switching.
        scores_by_game_button.configure(
            fg_color="#FFFFFF",
            command=lambda: switch_to_scores_by_game(team_data)
        )
        # endregion

        # region Display title configurations.

        # These need to be configured here so they can display the new, related titles.
        main_display_title.configure(
            text="Scoreboard"
        )

        main_display_subtitle.configure(
            text="Overall team scores"
        )

        # endregion

        # region Destroy previous frame
        # This needs to be done to be able to display the new frame.
        previous_data_frame.destroy()

        # endregion

        # region Scoreboard data frame
        team_data = ctk.CTkFrame(
            data_display_frame
        )

        team_data.pack(
            pady=20,
            padx=50,
            anchor="w"
        )

        display_csv_data(team_data, "teams", admin=False, sorted_data=True)

        # endregion

    def switch_to_scores_by_game(previous_data_frame):
        """
        Function that accounts for the scores by game button press.
        """

        # region Function to enable to CTk Tabview switches
        def tab_view_button_switch():

            # Retrieve name of current tab to pass through.
            current_tab = score_by_game_data.get()

            # Function to gather the required data to switch tabs.
            tab_switcher_data_gather(score_by_game_data.tab(current_tab), current_tab)

        # endregion

        # region Button and title configurations

        recent_match_result_button.configure(
            fg_color="#FFFFFF",
            command=lambda: create_user_page(parent)
        )

        scoreboard_button.configure(
            fg_color="#FFFFFF",
            command=lambda: switch_to_scoreboard(score_by_game_data)
        )

        scores_by_game_button.configure(
            fg_color="#F7F7F7",
            command=None
        )

        main_display_title.configure(
            text="Scores by game"
        )

        main_display_subtitle.configure(
            text="Team scores by game"
        )

        # endregion

        # region Destroy previous frame
        previous_data_frame.destroy()  # To ensure new data can be shown.

        # endregion

        # region Score by game tab view.
        score_by_game_data = ctk.CTkTabview(
            data_display_frame
        )

        # Retrieve tab view options from game_names CSV.
        tab_view_options = read_csv_column("game_names", 0)

        # Iterate over the options and display them as UX options for data display.
        for game_name in tab_view_options:
            score_by_game_data.add(game_name)
            score_by_game_data.configure(command=lambda: tab_view_button_switch(), text_color="#FFFFFF")
            tab_view_button_switch()

        score_by_game_data.pack(
            pady=20,
            padx=50,
            anchor="w"
        )

        # endregion

    # endregion

    # region Main user page frame configuration.
    user_page_frame = ctk.CTkFrame(
        parent,
        width=1040,
        height=560,
        corner_radius=0,
        border_width=0,
    )

    user_page_frame.grid(
        row=0,
        column=0,
        sticky="nsew",
        columnspan=2
    )
    # endregion

    # region Side / menu bar frame configuration.
    side_bar_frame = ctk.CTkFrame(
        user_page_frame,
        width=225,
        height=560,
        corner_radius=0,
        border_width=0,
        fg_color="#FFFFFF"
    )

    side_bar_frame.grid(
        row=0,
        column=0,
        sticky="ns"
    )

    # endregion

    # region Create CTk friendly images for use as icons
    home_icon = make_ctk_image("home.png", (18, 18))
    graph_icon = make_ctk_image("graph.png", (18, 18))
    by_game_icon = make_ctk_image("by_game.png", (18, 18))
    x_icon = make_ctk_image("x.png", (18, 18))
    # endregion

    # region User menu frame configuration
    user_menu_frame = ctk.CTkFrame(
        side_bar_frame,
        corner_radius=0,
        border_width=0,
        fg_color="#FFFFFF",
        bg_color="#FFFFFF"
    )

    user_menu_frame.grid(
        row=0,
        column=0,
        sticky="ne"
    )
    # endregion

    # region User menu frame widgets
    user_title_label = ctk.CTkLabel(
        user_menu_frame,
        text="E-SPORTS RESULTS TRACKER",
        font=("Inter", 16, "bold"),
        fg_color="#FFFFFF"
    )

    user_title_label.pack(
        pady=(50, 0),
        padx=25,
        anchor="center"
    )

    discover_text_label = ctk.CTkLabel(
        user_menu_frame,
        text="Discover",
        font=("Inter", 14, "bold")
    )

    discover_text_label.pack(
        pady=(20, 0),
        padx=25,
        anchor="w"
    )

    recent_match_result_button = ctk.CTkButton(
        user_menu_frame,
        text="Recent match results",
        width=200,
        height=30,
        corner_radius=8,
        fg_color="#F7F7F7",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        image=home_icon,
        compound="left",
        anchor="w"
    )

    recent_match_result_button.pack(
        pady=(15, 0),
        padx=15,
        anchor="w"
    )

    scoreboard_button = ctk.CTkButton(
        user_menu_frame,
        text="Scoreboard",
        width=200,
        height=30,
        corner_radius=8,
        fg_color="#FFFFFF",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        image=graph_icon,
        compound="left",
        anchor="w",
        command=lambda: switch_to_scoreboard(match_data)
    )

    scoreboard_button.pack(
        pady=(15, 0),
        padx=15,
        anchor="w"
    )

    scores_by_game_button = ctk.CTkButton(
        user_menu_frame,
        text="Scores by game",
        width=200,
        height=30,
        corner_radius=8,
        fg_color="#FFFFFF",
        hover_color="#F7F7F7",
        text_color="#000000",
        font=("Inter", 12),
        image=by_game_icon,
        compound="left",
        anchor="w",
        command=lambda: switch_to_scores_by_game(match_data)
    )

    scores_by_game_button.pack(
        pady=(15, 0),
        padx=15,
        anchor="w"
    )

    line = ctk.CTkCanvas(
        user_menu_frame,
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
        user_menu_frame,
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

    # region Main / data display frame configurations
    main_display_frame = ctk.CTkFrame(
        user_page_frame,
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

    # region Data display frame configurations
    data_display_frame = ctk.CTkFrame(
        main_display_frame,
        corner_radius=0,
        border_width=0,
        fg_color="#ECECEC",
        bg_color="#ECECEC"
    )

    data_display_frame.grid(
        row=0,
        column=0,
        sticky="nsew"
    )
    # endregion

    # region Information display frame widgets
    main_display_title = ctk.CTkLabel(
        data_display_frame,
        text="Recent match results",
        font=("Inter", 16, "bold")
    )

    main_display_title.pack(
        pady=(50, 5),
        padx=(50, 700),
        anchor="center"
    )

    main_display_subtitle = ctk.CTkLabel(
        data_display_frame,
        text="Covering the last 5 games",
        font=("Inter", 11),
        text_color="#454545"
    )

    main_display_subtitle.pack(
        padx=50,
        anchor="w"
    )

    match_data = ctk.CTkFrame(
        data_display_frame
    )

    match_data.pack(
        pady=20,
        padx=50,
        anchor="w"
    )

    display_csv_data(match_data, "match_data", False, True, 5)
    # endregion

    # region User page frame configurations
    user_page_frame.grid_rowconfigure(0, weight=1)
    user_page_frame.grid_columnconfigure(0, weight=1)
    user_page_frame.grid_columnconfigure(1, weight=1)
    # endregion

    # Return of the overall frame to ensure it displays correctly when called.
    return user_page_frame

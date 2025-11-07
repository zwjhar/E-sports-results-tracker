import customtkinter as ctk

from admin_page import create_admin_page
from functions.activate_placeholder import re_activate_placeholder
from functions.make_ctk_image import make_ctk_image
from functions.retrieve_and_format_entries import retrieve_entry
from user_page import create_user_page

# Function to initialise the main app window.
app = ctk.CTk()

# region Functions


def handle_admin_button_pressed(parent):
    """
    Function that handles when the admin button is pressed.
    """

    # Forget widgets to ensure they can be re-placed in their correct positions.
    disclaimer_label.pack_forget()
    or_continue_label.place_forget()
    admin_enter_button.pack_forget()

    # Create the password entry box and associated buttons.
    password_entry = ctk.CTkEntry(
        parent,
        width=250,
        height=30,
        corner_radius=8,
        font=("Inter", 12),
        fg_color="#FFFFFF",
        placeholder_text="Please enter the admin password...",
        placeholder_text_color="#828282",
        border_width=1,
        border_color="#E0E0E0",
        show="*"
    )
    password_entry.pack(
        pady=(20, 0),
        padx=133,
        anchor=ctk.N
    )

    # Create an error label but forget for now so that it can be used in the future.
    error_label = ctk.CTkLabel(
        parent,
        text="",
        text_color="red",
        font=("Inter", 10)
    )

    error_label.pack_forget()

    password_submit_button = ctk.CTkButton(
        parent,
        text="Proceed",
        width=250,
        height=30,
        corner_radius=8,
        fg_color="#EEEEEE",
        hover_color="#EEEEEE",
        text_color="#000000",
        font=("Inter", 12),
        # Pass through widgets that need to re-configured in the event of a change.
        command=lambda: verify_admin_password(password_entry, error_label, password_submit_button)
    )
    password_submit_button.pack(
        pady=(20, 0),
        padx=133,
        anchor="center"
    )

    # Re-place widgets in their correct sections.
    disclaimer_label.pack(
        pady=(15, 0),
        padx=157,
        anchor="center"
    )

    or_continue_label.place(
        relx=0.5,
        rely=0.63,
        anchor=ctk.N
    )


def verify_admin_password(password_entry, error_label, password_submit_button):
    """
    Function that verifies the admin password.
    """

    # Retrieve the password that has been entered to verify (see functions section)
    entry = retrieve_entry(password_entry)

    # Forget widgets so they can be re-placed in their correct section.
    password_submit_button.pack_forget()
    error_label.pack_forget()
    or_continue_label.place_forget()
    disclaimer_label.pack_forget()

    # Entry error checking - and a helpful reminder of what the error may be.
    if len(entry) == 0:
        error_label.configure(
            text="No password entered. Please try again.",
            pady=5
        )
        error_label.pack(pady=(5, 0), anchor="center")

        password_submit_button.pack(pady=(10, 0), padx=133, anchor="center")

    elif entry == "test":
        switch_frame(False)

    else:
        error_label.configure(
            text="Incorrect password. Please try again.",
            pady=5
        )
        error_label.pack(pady=(5, 0), anchor="center")

        password_submit_button.pack(pady=(10, 0), padx=133, anchor="center")

    # This code removes what has been placed in the password entry box. I
    re_activate_placeholder(password_entry, True)
    disclaimer_label.pack(pady=(15, 0), padx=157, anchor="center")

    or_continue_label.place(
        relx=0.5,
        rely=0.6,
        anchor=ctk.N
    )


def switch_frame(user=True):
    """
    Function to switch to user or admin related frames

    """

    login_page_left_frame.grid_forget()
    login_page_right_frame.grid_forget()

    if user:
        user_page_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    else:
        admin_page_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

# endregion

# region Application properties


app.geometry("1040x560")  # Set window size

# Set background colour.
app.config(bg="white")

# Set window title.
app.title("E-SPORTS Results App")

# Make the window so it can not be resized.
app.resizable(False, False)

# endregion

# region Left hand side of login screen - image

# Create login page left frame for the image (row 0, all columns).
login_page_left_frame = ctk.CTkFrame(
    app,
    width=450,
    height=760,
    corner_radius=0,
    border_width=0,
)

login_page_left_frame.grid(
    row=0,
    column=0,
    sticky="w"
)

# Load and place the desired image inside the frame.
image = make_ctk_image("computers.png", (450, 760))
image_place = ctk.CTkLabel(
    login_page_left_frame,
    image=image,
    text=""
)

image_place.grid(
    row=0,
    column=0,
    sticky="nw"
)

# endregion

# region Right hand side of login screen - widgets

# Create the login frame for the right hand side (row 1, all columns).
login_page_right_frame = ctk.CTkFrame(
    app,
    width=590,
    height=760,
    corner_radius=0,
    border_width=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF"
)

login_page_right_frame.grid(
    row=0,
    column=1,
    sticky="ne"
)

# Create the welcome titles to be placed one by one (on top of each other).
app_title_label = ctk.CTkLabel(
    login_page_right_frame,
    text="E-SPORTS RESULTS TRACKER",
    font=("Inter", 25, "bold"),
    fg_color="#FFFFFF"
)

app_title_label.pack(
    pady=(100, 0),
    padx=105,
    anchor="center"
)

app_welcome_label = ctk.CTkLabel(
    login_page_right_frame,
    text="Welcome to our application",
    font=("Inter", 18, "bold")
)

app_welcome_label.pack(
    pady=(30, 0),
    padx=177,
    anchor="center"
)

app_option_label = ctk.CTkLabel(
    login_page_right_frame,
    text="Please choose an option below",
    font=("Inter", 12)
)

app_option_label.pack(
    pady=(10, 0),
    padx=218,
    anchor="center"
)

# Create user interactive buttons to be placed on the page.

user_enter_button = ctk.CTkButton(
    login_page_right_frame,
    text="Enter our tracker",
    width=250,
    height=30,
    corner_radius=8,
    fg_color="#000000",
    hover_color="#000000",
    text_color="#FFFFFF",
    font=("Inter", 12),
    command=lambda: switch_frame()
)

user_enter_button.pack(
    pady=(15, 0),
    padx=133,
    anchor="center"
)

# Create the line effect to show a break between user and admin section - like a line break.

line = ctk.CTkCanvas(
    login_page_right_frame,
    bg="#FFFFFF",
    bd=0,
    highlightthickness=0,
    height=40
)

line.pack(
    pady=(25, 0),
    padx=100,
    anchor=ctk.N
)

line.create_line(0, 25, 650, 25, fill="#E6E6E6")

or_continue_label = ctk.CTkLabel(
    login_page_right_frame,
    text="   or continue to   ",
    font=("Inter", 12),
    text_color="#828282"
)

# This has to be placed so it sits on top of the line.

or_continue_label.place(
    relx=0.5,
    rely=0.71,
    anchor=ctk.N
)

# Create the administrator login options.

admin_enter_button = ctk.CTkButton(
    login_page_right_frame,
    text="Administration panel",
    width=250,
    height=30,
    corner_radius=8,
    fg_color="#EEEEEE",
    hover_color="#EEEEEE",
    text_color="#000000",
    font=("Inter", 12),
    command=lambda: handle_admin_button_pressed(login_page_right_frame)
)

admin_enter_button.pack(
    pady=(20, 0),
    padx=133,
    anchor="center"
)

# Create a disclaimer that advises people who are entering the application.

disclaimer_label = ctk.CTkLabel(
    login_page_right_frame,
    text="By proceeding, you agree to our Privacy Policy",
    font=("Inter", 12),
    text_color="#828282"
)

disclaimer_label.pack(
    pady=(15, 0),
    padx=157,
    anchor="center"
)

login_page_right_frame.grid_rowconfigure(0, weight=1)
login_page_right_frame.grid_columnconfigure(0, weight=1)

# endregion

# region App grid configurations

# Configure app's grid to make sure the regions expand.
app.grid_rowconfigure(0, weight=0)  # Image does not expand.

app.grid_columnconfigure(0, weight=0)  # Columns do not expand.
app.grid_columnconfigure(1, weight=0)

# endregion

# region Initialise user page

# Initialise and forget user page so it's there but doesn't appear - and can be called on when the button is pressed.
user_page_frame = create_user_page(app)
user_page_frame.grid_forget()

# endregion

# region Initialise admin page

# Initialise and forget admin page so it's there but doesn't appear - and can be called on when the button is pressed.
admin_page_frame = create_admin_page(app)
admin_page_frame.grid_forget()

# endregion

# Start the event loop.
app.mainloop()

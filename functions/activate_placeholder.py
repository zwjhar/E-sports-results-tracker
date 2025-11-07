import customtkinter as ctk


def re_activate_placeholder(entry_name, password=False):
    """

    The inspiration for the function below came from this gitHub entry:
    https://github.com/TomSchimansky/CustomTkinter/issues/2257

    """

    # Delete previous entry.
    entry_name.delete(0, ctk.END)
    # entry_name._activate_placeholder() - is a protected class so opted to take the approach below
    # which takes the placeholder text as it was set originally.

    # Set placeholder text back to previous entry.
    entry_name.configure(placeholder_text=f"{entry_name.cget("placeholder_text")}")
    # Re-focus placeholder.
    entry_name.master.focus()
    if password:
        entry_name.configure(
            show="*"  # Secures password entry integrity as it shows as "****"
        )

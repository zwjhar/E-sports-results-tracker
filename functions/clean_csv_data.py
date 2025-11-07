import pandas as pd


def clean_data(filename):
    """
    This function uses pandas to remove duplicates from entries.
    Simplifies the process of data validation when a new match is added.
    """
    df = pd.read_csv(f"{filename}.csv")  # Reads CSV
    df.dropna(inplace=True)  # Removes rows with no entries
    df.drop_duplicates(inplace=True)  # Remove rows that are duplicates
    df.to_csv(f"{filename}.csv", index=False)  # Save the cleaned data back to the CSV

import pandas as pd


def duplicate_csv_data(filename):
    """
    This function creates a duplicate of the specified csv file to help with data retention and to ensure data isn't
    lost if a csv is accidentally lost or deleted.

    It's much quicker and uses less code to use pandas to achieve this outcome.
    """
    df = pd.read_csv(f"{filename}.csv")  # Read CSV into a data frame
    df.to_csv("copy_of_" + f"{filename}.csv", index=False)  # Write a new CSV with the data called copy_of_XXX.

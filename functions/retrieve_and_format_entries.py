def retrieve_entry(entry):
    """
    This function retrieves an CTk entry and strips it of any whitespace for storage in the CSV.
    This ensures that duplicate entries can be searched against properly.
    """
    return entry.get().strip()  # Get entry and remove whitespaces.


def format_to_title_case(text):
    """
    This function converts an entry into proper title case, accounting that words like "of" and "and" don't need to be
    capitalised in an entry. It splits the text entry and formats them word by word as long as they don't appear in the
    exceptions list before returning the properly formatted entry.
    """

    exceptions = ["of", "and"]  # List of exceptions that should not be capitalised.

    words = text.split()  # Split the entry - so each word can be formatted individually.

    title_words = []  # Newly formatted string will be stored here.

    # Iterate through each word in the text that has been split.
    for i, word in enumerate(words):
        # If the word is an exception and isn't at the start or the end make it lowercase.
        if word.lower() in exceptions and i != 0 and i != len(words) - 1:
            title_words.append(word.lower())  # Add the word in lowercase.

        else:  # If not, capitalise the first letter and make the rest lowercase.
            title_words.append(word[0].upper() + word[1:].lower())

    return " ".join(title_words)  # Join the words and return the properly formatted string.

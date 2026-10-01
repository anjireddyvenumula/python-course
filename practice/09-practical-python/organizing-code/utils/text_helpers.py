# text_helpers.py
# Small, reusable functions for cleaning text.


def clean(text):
    """Strip whitespace and lowercase the text."""
    return text.strip().lower()


def word_count(text):
    """Count the words in a text."""
    return len(text.split())

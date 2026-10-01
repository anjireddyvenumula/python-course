# main.py
# Import your own functions from other files.
# Run it with: python main.py  (from any folder)

# Python looks for modules in the folder of the script you run,
# so the `utils` folder next to this file can be imported directly.
from utils.math_helpers import average, percentage
from utils.text_helpers import clean, word_count
import utils.text_helpers as text


def main():
    reviews = ["  GREAT course!  ", "Loved the examples", " Too short "]
    cleaned = [clean(review) for review in reviews]
    print("Cleaned:", cleaned)

    lengths = [word_count(review) for review in cleaned]
    print("Average words per review:", round(average(lengths), 2))
    print("Positive share:", percentage(2, len(reviews)), "%")
    print("Module-style call:", text.word_count("one two three"))


# This block only runs when you run the file directly, not when it is imported
if __name__ == "__main__":
    main()

# Try it:
# 1. Add a capitalize_words() function to text_helpers.py and use it here.
# 2. Create utils/date_helpers.py with a function that returns today's date.

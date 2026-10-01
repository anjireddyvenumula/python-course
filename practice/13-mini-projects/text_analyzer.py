# text_analyzer.py
# Practice: strings, dictionaries, sets, sorting and functions.
# Text analysis like this is a first step in many AI pipelines.

import re
from collections import Counter

STOP_WORDS = {"the", "a", "an", "and", "is", "in", "of", "to", "for", "it", "with", "on"}

SAMPLE_TEXT = """
Python is the most popular language for AI. Python is easy to read,
and the AI community builds many libraries with Python. Learning Python
is the first step to working with AI models, data and automation.
"""


def tokenize(text):
    """Lowercase the text and split it into words (letters only)."""
    return re.findall(r"[a-z]+", text.lower())


def analyze(text):
    words = tokenize(text)
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    meaningful = [w for w in words if w not in STOP_WORDS]
    return {
        "characters": len(text.strip()),
        "words": len(words),
        "unique_words": len(set(words)),
        "sentences": len(sentences),
        "avg_word_length": round(sum(len(w) for w in words) / len(words), 2),
        "top_words": Counter(meaningful).most_common(5),
    }


def print_report(stats):
    print("Text report")
    print("-" * 30)
    for key, value in stats.items():
        if key == "top_words":
            continue
        print(f"{key.replace('_', ' ').capitalize():<18} {value}")
    print("Top words:")
    for word, count in stats["top_words"]:
        print(f"  {word:<12} {'#' * count} ({count})")


if __name__ == "__main__":
    print_report(analyze(SAMPLE_TEXT))

# Try it:
# 1. Read the text from a .txt file instead of SAMPLE_TEXT.
# 2. Estimate the token count (a rough rule: words * 1.3).

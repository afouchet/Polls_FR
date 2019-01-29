"""
Clean text:
- Remove non alpha-numeric chars
- When a sentence has ended (has char "\n", ".", "!", etc), it's a new proposition
"""
import re


def get_clean_suggestion(text):
    char_end_prop = ".!?\n"
    # char_end_prop = "."
    lines = [text]
    for char in char_end_prop:
        lines = sum((l.split(char) for l in lines), [])
        # Keeping only lines that have at least 5 words
        lines = [l for l in lines if len(l.split()) > 4]

    return [get_clean_text(line) for line in lines]

def get_clean_text(text):
    return re.sub('[\W_]+', ' ', text)

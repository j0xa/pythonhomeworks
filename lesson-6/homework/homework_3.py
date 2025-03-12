import os
import string
from collections import Counter

FILE_NAME = "sample.txt"
REPORT_FILE = "word_count_report.txt"

def clean_text(text):
    """Removes punctuation and converts text to lowercase."""
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text.lower()

def get_text():
    """Reads the file or creates it if missing."""
    if not os.path.exists(FILE_NAME):
        print(f"'{FILE_NAME}' not found. Please enter text to create the file.")
        with open(FILE_NAME, "w") as file:
            text = input("Enter text for the file: ")
            file.write(text)
    with open(FILE_NAME, "r") as file:
        return file.read()

def count_words():
    """Counts word frequency and displays the top 5 words."""
    text = get_text()
    cleaned_text = clean_text(text)
    words = cleaned_text.split()
    
    if not words:
        print("The file is empty.")
        return
    
    word_count = Counter(words)
    total_words = sum(word_count.values())
    top_words = word_count.most_common(5)

    print(f"\nTotal words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_words:
        print(f"{word} - {count} times")

    save_report(total_words, top_words)

def save_report(total_words, top_words):
    """Saves word count results to a file."""
    with open(REPORT_FILE, "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n")
        file.write("Top 5 Words:\n")
        for word, count in top_words:
            file.write(f"{word} - {count}\n")
    print(f"\nWord count report saved to '{REPORT_FILE}'.")

# Run the program
count_words()
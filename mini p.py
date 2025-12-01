import string
from collections import Counter

def clean_text(text):
    text = text.lower()
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def scan_text(paragraph):
    cleaned = clean_text(paragraph)
    words = cleaned.split()

    words_list = words
    unique_words = set(words)
    frequency = Counter(words)

    if frequency:
        # ----- MOST FREQUENT WORDS -----
        max_count = max(frequency.values())
        most_common_words = [word for word, count in frequency.items() if count == max_count]

        # ----- LEAST FREQUENT WORDS -----
        min_count = min(frequency.values())
        least_common_words = [word for word, count in frequency.items() if count == min_count]
    else:
        most_common_words = []
        least_common_words = []

    total_words = len(words_list)
    total_unique_words = len(unique_words)

    return {
        "words_list": words_list,
        "unique_words": unique_words,
        "frequency": dict(frequency),
        "most_frequent": most_common_words,       # UPDATED
        "least_frequent": least_common_words,     # UPDATED
        "total_words": total_words,
        "total_unique_words": total_unique_words
    }

def report(data):
    with open("report.txt", "w") as f:
        f.write("TEXT ANALYSIS REPORT\n")
        f.write("====================\n\n")

        f.write(f"Total Words: {data['total_words']}\n")
        f.write(f"Total Unique Words: {data['total_unique_words']}\n\n")

        # MULTIPLE WORDS SUPPORTED
        f.write("Least Frequent Words: {}\n".format(", ".join(data['least_frequent'])))
        f.write("Most Frequent Words: {}\n\n".format(", ".join(data['most_frequent'])))

        f.write("Word Frequencies:\n")
        for word, freq in data['frequency'].items():
            f.write(f"{word}: {freq}\n")

        f.write("\nAll Words List:\n")
        f.write(", ".join(data['words_list']) + "\n")

        f.write("\nUnique Words Set:\n")
        f.write(", ".join(data['unique_words']) + "\n")


paragraph = input("Enter a paragraph of text:\n")
data = scan_text(paragraph)
report(data)

print("Report generated successfully as report.txt")

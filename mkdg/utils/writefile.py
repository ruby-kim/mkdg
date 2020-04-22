"""
Implement write misspelled files: csv, txt
"""
import csv


def save_csv_file(filename, texts):
    file_dir = "../../data/" + filename
    with open(file_dir, 'r') as f:
        writer = csv.writer(f)

        # default
        for text in texts:
            writer.writerow(text)


def save_text_file(filename):
    return


"""
Implement write misspelled files: csv, txt
"""
import csv
import os


def save_csv_file(filename, texts):
    filename = (os.getcwd() + filename).replace(".txt", "")
    filename += "_change"
    with open(filename, 'r') as f:
        writer = csv.writer(f)

        # default
        for text in texts:
            writer.writerow(text)


def save_text_file(filename, texts):
    filename = (os.getcwd() + "/data/" + filename).replace(".txt", "")
    print(filename)
    file = open(filename + "_change.txt", "w", encoding="utf-8")
    for text in texts:
        file.write(text)
    file.close()

"""
Implement write misspelled files: csv, txt
"""
import csv


def read_csv_file(filename, texts):
    file_dir = "../../data/" + filename
    with open(file_dir, 'r') as f:
        writer = csv.writer(f)

        # default
        for text in texts:
            writer.writerow(text)


def read_text_file(filename):
    filename = filename.replace(".txt", "")
    #dir = os.getcwd() + "\\"
    #file_dir = "../../data/" + filename
    file = open(filename + "_misspell.txt", 'w', encoding="utf-8")
    #for


"""
Implement load correct grammar file: csv, text
"""
import csv


def read_csv_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        print(reader)


def read_text_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.readlines()

    return text


if __name__ == "__main__":
    filename = "./data/20200404060046918.txt"
    raw_text = read_text_file(filename)
    print(raw_text)

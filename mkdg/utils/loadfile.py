"""
Implement load file: csv, text
"""
import pandas as pd


def read_csv_file(filename):
    data = pd.read_csv(filename)
    return data


def read_text_file(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.readlines()

    return text


if __name__ == "__main__":
    """ txt file """
    # filename = "./data/20200404060046918.txt"
    # raw_text = read_text_file(filename)
    # print(raw_text)

    """ csv file """
    filename = "./data/test.csv"
    raw_text = read_csv_file(filename)
    print(raw_text)


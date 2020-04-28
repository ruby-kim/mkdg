"""
Implement write misspelled files: csv, txt
"""
import csv
import os


def check_tgt_folder(targetPath):
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)


def save_csv_file(filename, texts):
    targetPath = os.getcwd() + "/data/tgt/"
    check_tgt_folder(targetPath)
    filename = (targetPath + filename).replace(".txt", "")

    with open(filename, 'r') as f:
        writer = csv.writer(f)
        # default
        for text in texts:
            writer.writerow(text)


def save_text_file(filename, texts):
    targetPath = os.getcwd() + "/data/tgt/"
    check_tgt_folder(targetPath)
    filename = (targetPath + filename).replace(".txt", "")

    file = open(filename + "_change.txt", "w", encoding="utf-8")
    for text in texts:
        file.write(text)
    file.close()

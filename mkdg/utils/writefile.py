"""
Implement write misspelled files: csv, txt
"""
import pandas as pd
import os


def check_tgt_folder(targetPath):
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)


def rewrite_xlxs_file(texts, len):
    targetPath = os.getcwd() + "/data/"
    check_tgt_folder(targetPath)
    print(targetPath)
    filename = targetPath + "misspell_origin.xlsx"
    df = pd.DataFrame(texts)
    print(texts)

    #print(df)
    #df.to_csv(filename, header=False, index=False)


def save_text_file(filename, texts, func=None):
    if func is None:
        targetPath = os.getcwd() + "/data/tgt/"
        check_tgt_folder(targetPath)
        filename = (targetPath + filename).replace(".txt", "")
        file = open(filename + "_change.txt", "w", encoding="utf-8")
    else:
        targetPath = os.getcwd() + "/data/analyze/"
        check_tgt_folder(targetPath)
        filename = (targetPath + filename).replace(".txt", "")
        if func is "morph":
            file = open(filename + "_morph.txt", "w", encoding="utf-8")
        elif func is "pos":
            file = open(filename + "_pos.txt", "w", encoding="utf-8")
        elif func is "origin":
            file = open(filename + "_origin.txt", "w", encoding="utf-8")

    for text in texts:
        file.write(text)
    file.close()

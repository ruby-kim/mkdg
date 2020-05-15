"""
Implement write misspelled files: csv, txt
"""
import pandas as pd
import numpy as np
import os


def check_tgt_folder(targetPath):
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)


def modify_dataframe(pastDataDict, newDictList):
    """
    Make new dataframe: connect [pastDataDict's value *-*-*-*-* newDictList's key

    Args:
        pastDataDict: origin xlsx data
        newDictList: want to add word list to xlsx file
    Returns:
        new dataframe which is conneted pastDataDict's value and newDictList's key
    """
    # df = pd.DataFrame.from_dict(pastDataDict)

    # find the length of all dictionary value's list
    max_len = 0
    for valList in pastDataDict.values():
        max_len = max(max_len, len(valList))

    # Resize all according to the determined max length
    for key, value in pastDataDict.items():
        if max_len != len(value):
            pastDataDict[key] = value.extend("None" * (max_len - len(value)))
        print(pastDataDict[key])

    # make past data dictionary to dataframe
    df = pd.DataFrame.from_dict(pastDataDict).T

    # change None value
    print(df.head())
    return df


def rewrite_xlxs_file(pastDataDict, newDictList):
    targetPath = os.getcwd() + "/data/"
    check_tgt_folder(targetPath)
    filename = targetPath + "misspell_origin.xlsx"
    df = modify_dataframe(pastDataDict, newDictList)
    df.to_csv(filename, mode="a", header=False)
    print("===== Finish: save new word list to data/misspell_origin.xlsx =====")


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

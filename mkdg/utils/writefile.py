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
    Make new dataframe: connect [pastDataDict's value *-*-*-*-* newDictList's key]

    Args:
        pastDataDict: origin xlsx data
        newDictList: want to add word list to xlsx file
    Returns:
        new dataframe which is connected pastDataDict's value and newDictList's key
    """

    # marge pastDataDict + newDictList values (change type to list for avoid runtime error)
    max_len = 0
    keyDataList = pastDataDict.keys()
    valDataList = pastDataDict.values()

    # find the longest length of value in dictionary to define column size
    for val in valDataList:
        max_len = max(max_len, len(val))

    # check word to insert pastDataDict
    for word in newDictList:
        if word not in keyDataList:
            pastDataDict[word] = list()

    # Resize all according to the determined max length
    for key, value in pastDataDict.items():
        if max_len != len(value):
            value += ["None"] * (max_len - len(value))
            pastDataDict[key] = value

    # make past data dictionary to dataframe & change "None" value to Nan
    df = pd.DataFrame.from_dict(pastDataDict).T
    df = df.replace("None", np.nan)

    # setting col(header) value
    col = []
    for i in range(1, max_len+1):
        col.append("change"+str(i))
    df.columns = col

    return df


def rewrite_xlxs_file(pastDataDict, newDictList, filename):
    targetPath = os.getcwd() + "/data/"
    check_tgt_folder(targetPath)
    filename = targetPath + filename
    modify_dataframe(pastDataDict, newDictList)
    df = modify_dataframe(pastDataDict, newDictList)
    df.to_excel(filename, index=True, header=True, index_label="origin")


def save_text_file(filename, texts, func=None):
    file = ""
    if func is None:
        targetPath = os.getcwd() + "/data/tgt/"
        check_tgt_folder(targetPath)
        filename = (targetPath + filename).replace(".txt", "")
        file = open(filename + "_change.txt", "w", encoding="utf-8")
    elif func is "user_dic":
        file = open(filename, "w", encoding="utf-8")
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

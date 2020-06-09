import os

from mkdg.utils.loadfile import read_text_file, read_xlsx_file
from mkdg.utils.writefile import save_text_file


def arrangement_text():
    data = read_text_file("user_dic.txt")
    mydict = dict()

    """ make dictionary key, value """
    for elem in data:
        elem = elem.replace("\n", "")
        if "\t" in elem:
            tmp = elem.split("\t")
            mydict[tmp[0]] = tmp[1]
        else:
            mydict[elem] = ""
    mydict = sorted(mydict.items())

    """ make dictionary to list """
    result = list()
    for elem in mydict:
        if elem[1] == "":
            result.append(elem[0]+"\n")
        else:
            result.append(elem[0]+"\t"+elem[1]+"\n")
    return result


def arrange_xlsx():
    data = read_xlsx_file("noun_standard")
    print(data)


def check_text_detail():
    data = read_text_file("user_dic.txt")
    for text in data:
        text = text.replace("\n", "")
        if '\t' in text:
            text = text.replace('\t', '<tab>')
        elif ' ' in text:
            text = text.replace(' ', '<space>')
        print(text)


def check_text_null():
    data = read_text_file("user_dic.txt")
    for text in data:
        if not text:
            break
        else:
            text = text.replace("\n", "")
            print(text)


if __name__ == "__main__":
    """ check null text """
    check_text_null()

    """ check detail text value """
    # check_text_detail()

    """ arrange user_dict.txt & save result """
    #result = arrangement_text()
    #save_text_file(os.getcwd() + "/user_dic.txt", result, "user_dic")

    """ arrange xlsx & save result """
    # arrange_xlsx()

import os

from mkdg.utils.loadfile import read_text_file
from mkdg.utils.writefile import save_text_file


def arrangement_text():
    data = read_text_file("data/user_dic.txt")
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
        if elem[1] is "":
            result.append(elem[0]+"\n")
        else:
            result.append(elem[0]+"\t"+elem[1]+"\n")
    return result


def check_null(data):
    for i in range(len(data)):
        print(i, data[i], end="")


if __name__ == "__main__":
    result = arrangement_text()
    # check_null(result)
    save_text_file(os.getcwd() + "/data/user_dic.txt", result, "user_dic")

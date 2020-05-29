import os

from mkdg.utils.loadfile import read_text_file
from mkdg.utils.writefile import save_text_file


def arrangement_text():
    data = read_text_file("data/user_dic.txt")
    mydict = dict()

    for i in range(len(data)):
        """ delete overlap word """
        unique_value = ""
        for j in data[i]:
            if j not in unique_value:
                unique_value += j
        """ make dictionary key, value """
        flag = False
        if " " in unique_value:
            tmp = unique_value.split(" ")
            flag = True
        elif "\t" in unique_value:
            tmp = unique_value.split("\t")
            flag = True
        else:
            tmp = unique_value

        if flag is True:
            mydict[tmp[0]] = tmp[1]
        else:
            mydict[tmp] = ""
    mydict = sorted(mydict.items())

    """ make dictionary to list """
    result = list()
    for elem in mydict:
        if elem[1] is "":
            result.append(elem[0])
        else:
            result.append(elem[0]+"\t"+elem[1])
    return result


if __name__ == "__main__":
    result = arrangement_text()
    save_text_file(os.getcwd() + "/data/user_dic.txt", result, "user_dic")

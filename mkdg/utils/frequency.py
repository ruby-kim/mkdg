"""
analyze top word frequency
"""
import re
from konlpy.tag import Komoran

from mkdg.loader.loadfile import read_text_file
from mkdg.utils.preprocess import del_special_char


def frequency(contents):
    """
    check word frequency

    Args:
        :param: contents(list)

    Returns:
        :param: word_dict(dict)
    """
    komoran = Komoran(userdic='./data/user_dic.txt')
    word_dict = dict()
    for text in contents:
        morList = komoran.morphs(text)
        for word in morList:
            word = re.sub("[ㄱ-ㅎ ㅏ-ㅣ 0-9]", repl="", string=word)
            if len(word) >= 2 and word is not "병":  # pass only one character(specific word)
                if word not in word_dict:
                    word_dict[word] = 0
                word_dict[word] += 1

    word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    print(word_dict[:20])


if __name__ == "__main__":
    filename = "20200404063414334.txt"
    path = "./data/" + filename
    raw_text = read_text_file(path)
    prep_text = del_special_char(raw_text)
    frequency(prep_text)

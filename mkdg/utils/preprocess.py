"""
Implement pre-process using regex
"""

import re


def del_special_char(text):
    """ ===================================
        전처리) 특수문자 제거:
            ~!@#$%^&*()_-+=|\[]{};':",./<>?
        ===================================
        Args:
            :param: text(list)

        Returns:
            전처리 한 text list
    """
    pattern = "[^\w\s]"
    repl = ""
    for i in range(len(text)):
        regexed_text = re.sub(pattern, repl, text[i])
        text[i] = regexed_text
    return text


def del_num(text):
    """ =======================
        전처리) 숫자 제거:
            0 1 2 3 4 5 6 7 8 9
        =======================
    Args:
        :param: text(list)

    Returns:
        전처리 한 text list
    """
    pattern = "[0-9]"
    repl = ""
    for i in range(len(text)):
        regexed_text = re.sub(pattern, repl, text[i])
        text[i] = regexed_text
    return text


def del_consonant(text):
    """ ==================================
        전처리) 자음 없애기
                ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅎ
        ==================================
        Args:
            :param: text(list)

        Returns:
            전처리 한 text list
        """
    pattern = "[0-9]"
    repl = ""
    for i in range(len(text)):
        regexed_text = re.sub(pattern, repl, text[i])
        text[i] = regexed_text
    return text


def del_alphabet(text):
    """ ==================================
        전처리) 알파벳 없애기
            소문자(a-z), 대문자(A-Z)
        ==================================
        Args:
            :param: text(list)

        Returns:
            전처리 한 text list
        """
    pattern = "[a-z A-Z]"
    repl = ""
    for i in range(len(text)):
        regexed_text = re.sub(pattern, repl, text[i])
        text[i] = regexed_text
    return text

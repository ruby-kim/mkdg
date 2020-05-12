"""
Implement pre-process using regex
"""

import re


def del_myregex(pattern, text):
    """ =======================================
        전처리) 원하는 문자 제거
        =======================================
        Args:
            :param: text(str)

        Returns:
            전처리 한 text(str)
    """
    regexed_text = re.compile(pattern).sub("", text)
    return regexed_text


def del_special_char(text):
    """ =======================================
        전처리) 특수문자 제거:
                ~!@#$%^&*()_-+=|\[]{};':",./<>?
        =======================================
        Args:
            :param: text(str)

        Returns:
            전처리 한 text(str)
    """

    pattern = "[^\w\s]"
    repl = ""
    regexed_text = re.compile(pattern).sub(repl, text)
    return regexed_text


def del_num(text):
    """ ===========================
        전처리) 숫자 제거:
                0 1 2 3 4 5 6 7 8 9
        ===========================
        Args:
            :param: text(str)

        Returns:
            전처리 한 text(str)
    """
    pattern = "[0-9]"
    repl = ""
    regexed_text = re.sub(pattern, repl, text)
    return regexed_text


def del_consonant(text):
    """ ==================================
        전처리) 자음 없애기
                ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅎ
        ==================================
        Args:
            :param: text(str)

        Returns:
            전처리 한 text(str)
    """
    pattern = "[ㄱ-ㅎ]"
    repl = ""
    regexed_text = re.sub(pattern, repl, text)
    return regexed_text


def del_vowel(text):
    """ ============================
        전처리) 모음 없애기
                ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ
        ============================
        Args:
            :param: text(str)

        Returns:
            전처리 한 text(str)
    """
    pattern = "[ㅏ-ㅣ]"
    repl = ""
    regexed_text = re.sub(pattern, repl, text)
    return regexed_text


def del_alphabet(text):
    """ ============================
        전처리) 알파벳 없애기
            소문자(a-z), 대문자(A-Z)
        ============================
        Args:
            :param: text(str)

        Returns:
            전처리 한 text(str)
    """
    pattern = "[a-z A-Z]"
    repl = ""
    regexed_text = re.sub(pattern, repl, text)
    return regexed_text


if __name__ == "__main__":
    test_consonant = "아악ㄱㄱㄱ너무ㄱㄱ맛ㅅ있당ㅇ"
    print(del_consonant(test_consonant))

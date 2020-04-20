"""
Implement pre-process using regex
"""

import re


def preprocess(text):
    """ ===================================
        전처리) 특수문자 제거:
            ~!@#$%^&*()_-+=|\[]{};':",./<>?
        ===================================
        Args:
            text(list type):

        Returns:
            전처리 한 text list
    """
    pattern = "[^\w\s]"
    repl = ""
    for i in range(len(text)):
        regexed_text = re.sub(pattern, repl, text[i])
        text[i] = regexed_text
    return text

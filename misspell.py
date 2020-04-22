# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement making misspelled korean data operator
"""

from mkdg.option import setting_parse
from mkdg.loader.loadfile import read_text_file
from mkdg.utils.preprocess import del_special_char


if __name__ == '__main__':
    """ Setting parameters input & description """
    #filename = setting_parse()
    filename = "20200404060046918.txt"
    path = "./data/" + filename
    raw_text = read_text_file(path)
    prep_text = del_special_char(raw_text)


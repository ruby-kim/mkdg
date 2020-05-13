# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implement making misspelled korean data operator
"""
import re

from mkdg.utils.loadfile import read_text_file
from mkdg.misspell.origin import load_origin
from mkdg.utils.getmisspell import misspell_all_data
from mkdg.utils.chgword import chg_word
from mkdg.utils.writefile import save_text_file


def based_on_tag(filename, raw_text):
    """ based on tag (data/misspell_stem.xlsx) """
    # 1) get mis-spell data
    adjective, adjective_alt, \
    adverb, adverb_alt, \
    conjunction, conjunction_alt, \
    determiner, determiner_alt, \
    eomi, eomi_alt, \
    josa, josa_alt, \
    noun, noun_alt, \
    preEomi, preEomi_alt, \
    suffix, suffix_alt, \
    verb, verb_alt = misspell_all_data()

    # 2) make mis-spell contents
    result = chg_word(raw_text, adjective, adjective_alt)
    result = chg_word(result, adverb, adverb_alt)
    result = chg_word(result, conjunction, conjunction_alt)
    result = chg_word(result, determiner, determiner_alt)
    result = chg_word(result, eomi, eomi_alt)
    result = chg_word(result, josa, josa_alt)
    result = chg_word(result, noun, noun_alt)
    result = chg_word(result, preEomi, preEomi_alt)
    result = chg_word(result, suffix, suffix_alt)
    result = chg_word(result, verb, verb_alt)
    save_text_file(filename, result)


def based_on_origin_word(filename, raw_text):
    """ based on origin word (data/misspell_origin.xlsx) """
    origin = load_origin()
    result = chg_word(raw_text, origin)
    save_text_file(filename, result)


if __name__ == '__main__':
    """ Setting parameters input & description """
    # filename = setting_parse()
    filename = "J 민원 교통_최종본(0416)_only_speak.txt"
    path = "./data/" + filename
    raw_text = read_text_file(path)
    for i in range(len(raw_text)):
        text = re.sub("[ㄱ-ㅎ|ㅏ-ㅣ|.,?!]", "", raw_text[i])
        raw_text[i] = text

    """ use [data/misspell_origin.xlsx] """
    based_on_origin_word(filename, raw_text)

    """ use [data/misspell_stem.xlsx] """
    # based_on_tag(filename, raw_text)

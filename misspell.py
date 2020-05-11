# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2020 by Kyeong-nam Kim <kkyy0126@naver.com>

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the “Software”), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

"""
Implement making misspelled korean data operator
"""
import re

from mkdg.utils.loadfile import read_text_file
from mkdg.utils.getmisspell import misspell_all_data
from mkdg.utils.chgword import chg_word
from mkdg.utils.writefile import save_text_file


if __name__ == '__main__':
    """ Setting parameters input & description """
    #filename = setting_parse()
    filename = "F 카페(7,859)_only_speak.txt"
    path = "./data/" + filename
    raw_text = read_text_file(path)
    for i in range(len(raw_text)):
        text = re.sub("[ㄱ-ㅎ|ㅏ-ㅣ|.,?!]", "", raw_text[i])
        raw_text[i] = text

    """ get mis-spell data """
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

    """ make mis-spell contents """
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

# !/usr/bin/env python
# -*- coding: utf-8 -*-

__name__ = 'mkdg'
__description__ = 'Misspelled Korean Data Generator'
__version__ = '0.0.0'
__url__ = 'https://github.com/study-ai-data/mkdg'
__download_url__ = 'https://github.com/study-ai-data/mkdg'
__install_requires__ = [
    "konlpy",   # komoran
    "pandas",
    "xlrd",
    "soyspacing",
    "numpy",
    "korNum",
    "py-hanspell"
]
__license__ = 'MIT'


from mkdg.option import *
from mkdg.misspell import *
from mkdg.utils import *

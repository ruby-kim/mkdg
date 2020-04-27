"""
analyze top word frequency
"""
import re
from konlpy.tag import Komoran

from mkdg.utils.loadfile import read_text_file


def tag_switch(tag):
    """
    classify tag names

    Args:
        :param: tag(str)

    Returns:
        :param: tag name(str)
    """
    return{
        "VA" or "VCN" or "VCP": "adjective",
        "MAG": "adverb",
        "MAJ": "conjunction",
        "MM": "determiner",
        "EC" or "EF" or "ETM" or "ETN": "eomi",
        "JC" or "JKC" or "JKG" or "JKV" or "JKB" or "JKO" or "JKQ" or "JKS" or "JS": "josa",
        "NNG" or "NNB" or "NNP" or "NP" or "NR": "noun",
        "EP": "preEomi",
        "XPN" or "XSA" or "XSN" or "XSV": "suffix",
        "VV" or "VX": "verb"
    }.get(tag, -1)


def tag_cnt(word, tag_dict):
    """
    check word existence in tag_dict & count word

    Args:
        :param: word(str)
        :param: tag_dict(dictionary)

    Returns:
        :param: tag_dict(dictionary)
    """
    if word not in tag_dict:
        tag_dict[word] = 0
    tag_dict[word] += 1
    return tag_dict


def frequency(contents):
    """
    check word frequency

    Args:
        :param: contents(list)

    Returns:
        :param: word_dict(dict)
    """
    komoran = Komoran(userdic='./data/user_dic.txt')

    adjective_dict = dict()     # 형용사: VA, VCN, VCP
    adverb_dict = dict()        # 부사: MAG
    conjunction_dict = dict()   # 접속사: MAJ
    determiner_dict = dict()    # 관형사: MM
    eomi_dict = dict()          # 어미: EC, EF, ETM, ETN
    josa_dict = dict()          # 조사: JC, JKC, JKG, JKV, JKB, JKO, JKQ, JKS, JX
    noun_dict = dict()          # 명사: NNG, NNB, NNP, NP, NR
    preEomi_dict = dict()       # 선어말어미: EP
    suffix_dict = dict()        # 접사: XPN, XSA, XSN, XSV
    verb_dict = dict()          # 동사: VV, VX

    for text in contents:
        posList = komoran.pos(text)
        for pos in posList:
            # preprocessing
            word = re.sub("[ㄱ-ㅎ|ㅏ-ㅣ|.,?!]", repl="", string=str(pos[0]))
            if word == "":
                continue

            # seperate tag & count
            tagName = tag_switch(pos[1])
            if tagName != -1:
                if tagName == "adjective":
                    adjective_dict = tag_cnt(word, adjective_dict)
                elif tagName == "adverb":
                    adverb_dict = tag_cnt(word, adverb_dict)
                elif tagName == "conjunction":
                    conjunction_dict = tag_cnt(word, conjunction_dict)
                elif tagName == "determiner":
                    determiner_dict = tag_cnt(word, determiner_dict)
                elif tagName == "eomi":
                    eomi_dict = tag_cnt(word, eomi_dict)
                elif tagName == "josa":
                    josa_dict = tag_cnt(word, josa_dict)
                elif tagName == "noun":
                    noun_dict = tag_cnt(word, noun_dict)
                elif tagName == "preEomi":
                    preEomi_dict = tag_cnt(word, preEomi_dict)
                elif tagName == "suffix":
                    suffix_dict = tag_cnt(word, suffix_dict)
                elif tagName == "verb":
                    verb_dict = tag_cnt(word, verb_dict)

    # sorting by cnt
    adjective_dict = sorted(adjective_dict.items(), key=lambda x: x[1], reverse=True)
    adverb_dict = sorted(adverb_dict.items(), key=lambda x: x[1], reverse=True)
    conjunction_dict = sorted(conjunction_dict.items(), key=lambda x: x[1], reverse=True)
    determiner_dict = sorted(determiner_dict.items(), key=lambda x: x[1], reverse=True)
    eomi_dict = sorted(eomi_dict.items(), key=lambda x: x[1], reverse=True)
    josa_dict = sorted(josa_dict.items(), key=lambda x: x[1], reverse=True)
    noun_dict = sorted(noun_dict.items(), key=lambda x: x[1], reverse=True)
    preEomi_dict = sorted(preEomi_dict.items(), key=lambda x: x[1], reverse=True)
    suffix_dict = sorted(suffix_dict.items(), key=lambda x: x[1], reverse=True)
    verb_dict = sorted(verb_dict.items(), key=lambda x: x[1], reverse=True)

    print("형용사:")
    print(adjective_dict[:30])
    print("\n부사:")
    print(adverb_dict[:30])
    print("\n접속사:")
    print(conjunction_dict[:30])
    print("\n관형사:")
    print(determiner_dict[:30])
    print("\n어미:")
    print(eomi_dict[:30])
    print("\n조사:")
    print(josa_dict[:30])
    print("\n명사:")
    print(noun_dict[:30])
    print("\n선어말어미:")
    print(preEomi_dict[:30])
    print("\n접사:")
    print(suffix_dict[:30])
    print("\n동사:")
    print(verb_dict[:30])


if __name__ == "__main__":
    filename = "A 음식점(15,726)_only_speak.txt"
    path = "./data/" + filename
    raw_text = read_text_file(path)
    frequency(raw_text)


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
    return {
        "VA" or "VCN" or "VCP": "adjective",    # 형용사
        "MAG": "adverb",    # 부사
        "MAJ": "conjunction",   # 접속사
        "MM": "determiner", # 관형사
        "EC" or "EF" or "ETM" or "ETN": "eomi", # 어미
        "JC" or "JKC" or "JKG" or "JKV" or "JKB" or "JKO" or "JKQ" or "JKS" or "JS": "josa",    # 조사
        "NNG" or "NNB" or "NNP" or "NP" or "NR": "noun",    # 명사
        "EP": "preEomi",    # 선어말어미
        "XPN" or "XSA" or "XSN" or "XSV": "suffix", # 접사
        "VV" or "VX": "verb"    # 동사
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


class Tag_dict:
    def __init__(self, content):
        self.content = content
        self.komoran = Komoran(userdic='./data/user_dic.txt')
        self.adjective_dict = dict()  # 형용사: VA, VCN, VCP
        self.adverb_dict = dict()  # 부사: MAG
        self.conjunction_dict = dict()  # 접속사: MAJ
        self.determiner_dict = dict()  # 관형사: MM
        self.eomi_dict = dict()  # 어미: EC, EF, ETM, ETN
        self.josa_dict = dict()  # 조사: JC, JKC, JKG, JKV, JKB, JKO, JKQ, JKS, JX
        self.noun_dict = dict()  # 명사: NNG, NNB, NNP, NP, NR
        self.preEomi_dict = dict()  # 선어말어미: EP
        self.suffix_dict = dict()  # 접사: XPN, XSA, XSN, XSV
        self.verb_dict = dict()  # 동사: VV, VX

    def print_frequency(self, cnt=30):
        """
            print dict values frequency (descending)

            Args:
                :param: cnt(int)
            Returns:
                :param: tagDict(1st ~ until cnt-th) (dict)
        """
        self.adjective_dict = sorted(self.adjective_dict.items(), key=lambda x: x[1], reverse=True)
        self.adverb_dict = sorted(self.adverb_dict.items(), key=lambda x: x[1], reverse=True)
        self.conjunction_dict = sorted(self.conjunction_dict.items(), key=lambda x: x[1], reverse=True)
        self.determiner_dict = sorted(self.determiner_dict.items(), key=lambda x: x[1], reverse=True)
        self.eomi_dict = sorted(self.eomi_dict.items(), key=lambda x: x[1], reverse=True)
        self.josa_dict = sorted(self.josa_dict.items(), key=lambda x: x[1], reverse=True)
        self.noun_dict = sorted(self.noun_dict.items(), key=lambda x: x[1], reverse=True)
        self.preEomi_dict = sorted(self.preEomi_dict.items(), key=lambda x: x[1], reverse=True)
        self.suffix_dict = sorted(self.suffix_dict.items(), key=lambda x: x[1], reverse=True)
        self.verb_dict = sorted(self.verb_dict.items(), key=lambda x: x[1], reverse=True)

        print("형용사:")
        print(self.adjective_dict[:cnt])
        print("\n부사:")
        print(self.adverb_dict[:cnt])
        print("\n접속사:")
        print(self.conjunction_dict[:cnt])
        print("\n관형사:")
        print(self.determiner_dict[:cnt])
        print("\n어미:")
        print(self.eomi_dict[:cnt])
        print("\n조사:")
        print(self.josa_dict[:cnt])
        print("\n명사:")
        print(self.noun_dict[:cnt])
        print("\n선어말어미:")
        print(self.preEomi_dict[:cnt])
        print("\n접사:")
        print(self.suffix_dict[:cnt])
        print("\n동사:")
        print(self.verb_dict[:cnt])

    def judge_tag(self):
        for text in self.content:
            posList = self.komoran.pos(text)
            for pos in posList:
                # preprocessing
                word = re.sub("[ㄱ-ㅎ|ㅏ-ㅣ|.,?!]", repl="", string=str(pos[0]))
                if word == "":
                    continue

                # seperate tag & count
                tagName = tag_switch(pos[1])
                if tagName != -1:
                    if tagName == "adjective":
                        self.adjective_dict = tag_cnt(word, self.adjective_dict)
                    elif tagName == "adverb":
                        self.adverb_dict = tag_cnt(word, self.adverb_dict)
                    elif tagName == "conjunction":
                        self.conjunction_dict = tag_cnt(word, self.conjunction_dict)
                    elif tagName == "determiner":
                        self.determiner_dict = tag_cnt(word, self.determiner_dict)
                    elif tagName == "eomi":
                        self.eomi_dict = tag_cnt(word, self.eomi_dict)
                    elif tagName == "josa":
                        self.josa_dict = tag_cnt(word, self.josa_dict)
                    elif tagName == "noun":
                        self.noun_dict = tag_cnt(word, self.noun_dict)
                    elif tagName == "preEomi":
                        self.preEomi_dict = tag_cnt(word, self.preEomi_dict)
                    elif tagName == "suffix":
                        self.suffix_dict = tag_cnt(word, self.suffix_dict)
                    elif tagName == "verb":
                        self.verb_dict = tag_cnt(word, self.verb_dict)


def frequency(contents):
    """
    check word frequency

    Args:
        :param: contents(list)
    Returns:
        :param: word_dict(dict)
    """
    dict = Tag_dict(contents)
    dict.judge_tag()
    dict.print_frequency()


if __name__ == "__main__":
    filename = "A 음식점(15,726)_only_speak.txt"
    path = "./data/" + filename
    raw_text = read_text_file(path)
    frequency(raw_text)

# -*- coding: utf-8 -*-
"""
analyze sentences & top word frequency
"""
import re
import os
from konlpy.tag import Komoran
from soyspacing.countbase import CountSpace

from mkdg.utils.loadfile import read_text_file, read_xlsx_file
from mkdg.utils.writefile import save_text_file, rewrite_xlxs_file
from mkdg.utils.preprocess import del_special_char


def tag_switch(tag):
    """
    classify tag names

    Args:
        :param: tag(str)
    Returns:
        :param: tag name(str)
    """
    if (tag == "NNP") or (tag == "NNB") or (tag == "NNG") or (tag == "NP") or (tag == "NR"):    # 명사
        return "noun"
    elif (tag == "VA") or (tag == "VCN") or (tag == "VCP"):   # 형용사
        return "adjective"
    elif (tag == "EC") or (tag == "EF") or (tag == "ETM") or (tag == "ETN"):   # 어미
        return "eomi"
    elif (tag == "JC") or (tag == "JKC") or (tag == "JKG") or (tag == "JKV") or (tag == "JKB") or (tag == "JKO") or (tag == "JKQ") or (tag == "JKS") or (tag == "JS"):  # 조사
        return "josa"
    elif (tag == "XPN") or (tag == "XSA") or (tag == "XSN") or (tag == "XSV"):     # 접사
        return "suffix"
    elif (tag == "VV") or (tag == "VX"):     # 동사
        return "verb"
    elif tag == "MAG":  # 부사
        return "adverb"
    elif tag == "MAJ":  # 접속사
        return "conjunction"
    elif tag == "MM":   # 관형사
        return "determiner"
    elif tag == "EP":   # 선어말어미
        return "preEomi"
    else:
        return -1


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
        self.komoran = Komoran(userdic=os.getcwd()+'/user_dic.txt')
        self.model = CountSpace()
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
        self.wordDict = dict()

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

    def cnt_origin_word(self):
        if type(self.wordDict) is list:
            return
        for text in self.content:
            sent_corrected, tags = self.model.correct(text)
            words = del_special_char(sent_corrected).split(" ")
            for word in words:
                if word not in self.wordDict.keys():
                    self.wordDict[word] = 0
                self.wordDict[word] += 1

    def print_len(self):
        print("text line:", len(self.content))

    def print_noun_list(self):
        self.judge_tag()
        print(self.noun_dict)

    def print_tag_frequency(self, cnt=30):
        """
        print dict values frequency (descending)

        Args:
            :param: cnt(int)
        Returns:
            :param: tagDict(1st ~ until cnt-th) (dict)
        """
        self.judge_tag()

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

        print("형용사(adjective):")
        print(self.adjective_dict[:cnt])
        print("\n부사(adverb):")
        print(self.adverb_dict[:cnt])
        print("\n접속사(conjunction):")
        print(self.conjunction_dict[:cnt])
        print("\n관형사(determiner):")
        print(self.determiner_dict[:cnt])
        print("\n어미(eomi):")
        print(self.eomi_dict[:cnt])
        print("\n조사(josa):")
        print(self.josa_dict[:cnt])
        print("\n명사(noun):")
        print(self.noun_dict[:cnt])
        print("\n선어말어미(preEomi):")
        print(self.preEomi_dict[:cnt])
        print("\n접사(suffix):")
        print(self.suffix_dict[:cnt])
        print("\n동사(verb):")
        print(self.verb_dict[:cnt])

    def print_origin_frequency(self, cnt=30):
        """
        print origin values frequency (descending)

        Args:
            :param: cnt(int)
        """
        self.cnt_origin_word()
        self.wordDict = sorted(self.wordDict.items(), key=lambda x: x[1], reverse=True)
        print(self.wordDict[:cnt])

    def print_dict(self, tagName):
        self.judge_tag()

        if tagName == "adjective":
            for tag in self.adjective_dict.keys():
                print(tag)
        elif tagName == "adverb":
            for tag in self.adverb_dict.keys():
                print(tag)
        elif tagName == "conjunction":
            for tag in self.conjunction_dict.keys():
                print(tag)
        elif tagName == "determiner":
            for tag in self.determiner_dict.keys():
                print(tag)
        elif tagName == "eomi":
            for tag in self.eomi_dict.keys():
                print(tag)
        elif tagName == "josa":
            for tag in self.josa_dict.keys():
                print(tag)
        elif tagName == "noun":
            for tag in self.noun_dict.keys():
                print(tag)
        elif tagName == "preEomi":
            for tag in self.preEomi_dict.keys():
                print(tag)
        elif tagName == "suffix":
            for tag in self.suffix_dict.keys():
                print(tag)
        elif tagName == "verb":
            for tag in self.verb_dict.keys():
                print(tag)

    def print_morph(self):
        for text in self.content:
            result = self.komoran.morphs(text)
            print(result)

    def print_pos(self):
        for text in self.content:
            result = self.komoran.pos(text)
            print(result)

    def save_compare(self, form):
        result = ""
        if form is "morph":
            for text in self.content:
                result += text + str(self.komoran.morphs(text)) + "\n\n"
        elif form is "pos":
            for text in self.content:
                result += text + str(self.komoran.pos(text)) + "\n\n"

        save_text_file(filename, result, form)

    def save_origin_frequency(self):
        result = ""
        self.judge_tag()
        self.cnt_origin_word()
        if type(self.wordDict) is dict:
            self.wordDict = sorted(self.wordDict.items(), key=lambda x: x[1], reverse=True)

        """ save result as .txt """
        for key_value in self.wordDict:
            result += str(key_value) + "\n"
        save_text_file(filename, result, "origin")

        """ save new word dict to misspell_origin.xlsx """
        # load existence values & make as a dictionary
        pastData = read_xlsx_file()
        pastDataDict = dict()
        for i in range(pastData.shape[0]):
            valList = list()
            for j in range(1, pastData.shape[1]):
                if type(pastData.loc[i][j]) is str:
                    valList.append(pastData.loc[i][j])
                else:
                    break
            pastDataDict[pastData.loc[i][0]] = valList
        pastData_keyList = list(pastDataDict.keys())  # for delete overlap word

        # make current values as a list
        current_data_list = list(dict(self.wordDict).keys())

        # make new dict list (delete overlap word)
        newDictList = list(set(pastData_keyList + current_data_list))
        newDictList.remove("")  # delete empty element

        # re-write contents (data/misspell_origin.xlsx)
        rewrite_xlxs_file(pastDataDict, newDictList, "misspell_origin.xlsx")
        print("===== Finish: save new word list to data/misspell_origin.xlsx =====")

    def save_noun_standard(self):
        # count origin word frequency
        self.judge_tag()
        self.cnt_origin_word()
        if type(self.wordDict) is dict:
            self.wordDict = sorted(self.wordDict.items(), key=lambda x: x[1], reverse=True)

        # load existence values & make as a dictionary
        pastData = read_xlsx_file("noun_standard")
        pastDataDict = dict()
        for i in range(pastData.shape[0]):
            valList = list()
            for j in range(1, pastData.shape[1]):
                if type(pastData.loc[i][j]) is str:
                    valList.append(pastData.loc[i][j])
                else:
                    break
            pastDataDict[pastData.loc[i][0]] = valList
        pastData_keyList = list(pastDataDict.keys())  # for delete overlap word

        # make current values as a list
        current_data_list = list()
        for noun in self.noun_dict.keys():
            current_data_list.append(noun)
        for key_value in self.wordDict:
            tmp = key_value[0]
            for noun in current_data_list:
                if noun in key_value[0]:
                    tmp = tmp.replace(noun, "")
            if tmp != "":
                current_data_list.append(tmp)

        # make new dict list (delete overlap word)
        newDictList = list(set(pastData_keyList + current_data_list))
        if "" in newDictList:
            newDictList.remove("")  # delete empty element

        # re-write contents (data/misspell_origin.xlsx)
        rewrite_xlxs_file(pastDataDict, newDictList, "misspell_noun_standard.xlsx")
        print("===== Finish: save new word list to data/misspell_noun_standard.xlsx =====")


def analyze(contents):
    """
    analyze texts

    Args:
        :param: contents(list)
    Returns:
        :param: word_dict(dict)
    """
    dict = Tag_dict(contents)             # initial dict class
    # dict.print_len()                    # print context count
    # dict.print_origin_frequency()       # print origin frequency words count (default: 30)
    # dict.print_morph()                  # print morph text
    # dict.print_pos()                    # print pos text
    # dict.print_tag_frequency()          # print top tag frequency words count (default: 30)
    # dict.print_dict("noun")             # print selected tag list
    # dict.save_compare("morph")          # save all of origin text & morph text
    # dict.save_compare("pos")            # save all of origin text & pos text
    dict.save_noun_standard()             # save all of origin noun & etc words
    # dict.save_origin_frequency()        # save all of origin frequency words count
    print(dict.noun_dict)


if __name__ == "__main__":
    filename = "J 민원 차량등록_최종본(0429)_only_speak_naver.txt"
    path = "./data/" + filename
    raw_text = read_text_file(path)
    analyze(raw_text)

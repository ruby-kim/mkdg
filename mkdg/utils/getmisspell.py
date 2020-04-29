from mkdg.misspell.adjective import load_adjective
from mkdg.misspell.adverb import load_adverb
from mkdg.misspell.conjunction import load_conjunction
from mkdg.misspell.determiner import load_determiner
from mkdg.misspell.eomi import load_eomi
from mkdg.misspell.josa import load_josa
from mkdg.misspell.noun import load_noun
from mkdg.misspell.preEomi import load_preEomi
from mkdg.misspell.suffix import load_suffix
from mkdg.misspell.verb import load_verb

from mkdg.utils.loadfile import read_csv_file


def misspell_single_data(filename):
    """
    Get mis-spell dictionary, key: origin / value: change word list
        Args:
            :param: filename(str): the path of file
        Returns:
            :param: misspell(dict): mis-spell dictionary (from .csv file)
    """
    data = read_csv_file(filename)

    misspell = dict()   # mis-spell dictionary

    for i in range(data.shape[0]):
        chgWord = list()  # change word list
        for j in range(1, data.shape[1]):
            if type(data.loc[i][j]) is str:
                if j == 1:  # Add origin word
                    chgWord.append(data.loc[i][0])
                else:
                    chgWord.append(data.loc[i][j])
            else:
                if j == 1:
                    chgWord.append(data.loc[i][0])
                break
        misspell[data.loc[i][0]] = chgWord
    return misspell


def misspell_all_data():
    """
    Get all of mis-spell dictionaries, key: origin / value: change word list
        Returns:
            :param: all of mis-spell dictionaries & alternative list
    """
    adjective, adjective_alt = load_adjective()
    adverb, adverb_alt = load_adverb()
    conjunction, conjunction_alt = load_conjunction()
    determiner, determiner_alt = load_determiner()
    eomi, eomi_alt = load_eomi()
    josa, josa_alt = load_josa()
    noun, noun_alt = load_noun()
    preEomi, preEomi_alt = load_preEomi()
    suffix, suffix_alt = load_suffix()
    verb, verb_alt = load_verb()
    return \
        adjective, adjective_alt,\
        adverb, adverb_alt,\
        conjunction, conjunction_alt,\
        determiner, determiner_alt,\
        eomi, eomi_alt,\
        josa, josa_alt,\
        noun, noun_alt,\
        preEomi, preEomi_alt,\
        suffix, suffix_alt,\
        verb, verb_alt


if __name__ == "__main__":
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

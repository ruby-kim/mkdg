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


def misspell_data():
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
    verb, verb_alt = misspell_data()

    print(noun)

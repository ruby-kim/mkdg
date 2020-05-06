"""
명사
"""
from mkdg.utils.chgword import chg_word


def load_noun():
    from mkdg.utils.getmisspell import misspell_single_data
    """
    Load noun data

    Returns: noun dictionary, alternative list
    """
    noun = misspell_single_data("noun")
    alternative = {

    }
    return noun, alternative


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)
    noun, alt = load_noun()
    result = chg_word(test, noun)  # , alt)
    print("Result: ", result)

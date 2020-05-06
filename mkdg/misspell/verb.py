"""
동사
"""
from mkdg.utils.chgword import chg_word


def load_verb():
    from mkdg.utils.getmisspell import misspell_single_data
    """
    Load verb data

    Returns: verb dictionary, alternative list
    """
    verb = misspell_single_data("verb")
    alternative = {
        "습니다": "니다"
    }
    return verb, alternative


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]
    print("Origin: ", test)
    verb, alt = load_verb()
    result = chg_word(test, verb, alt)
    print("Result: ", result)

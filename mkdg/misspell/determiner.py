"""
관형사
"""
from mkdg.utils.chgword import chg_word


def load_determiner():
    from mkdg.utils.getmisspell import misspell_single_data
    """
    Load determiner data

    Returns: determiner dictionary, alternative list
    """
    determiner = misspell_single_data("determiner")
    alternative = {

    }
    return determiner, alternative


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)
    determiner, alternative = load_determiner()
    result = chg_word(test, determiner)  # , alt)
    print("Result: ", result)


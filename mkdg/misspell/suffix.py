"""
접사
"""
from mkdg.utils.chgword import chg_word


def load_suffix():
    from mkdg.utils.getmisspell import misspell_single_data
    """
    Load suffix data

    Returns: suffix dictionary, alternative list
    """
    filename = "data/suffix.csv"
    suffix = misspell_single_data(filename)
    alternative = {

    }
    return suffix, alternative


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)
    suffix, alt = load_suffix()
    result = chg_word(test, suffix)  # , alt)
    print("Result: ", result)

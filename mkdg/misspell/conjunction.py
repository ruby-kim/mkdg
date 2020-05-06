"""
접속사
"""
from mkdg.utils.chgword import chg_word


def load_conjunction():
    from mkdg.utils.getmisspell import misspell_single_data
    """
    Load conjunction data

    Returns: conjunction dictionary, alternative list
    """
    conjunction = misspell_single_data("conjunction")
    alternative = {
        "그러면": "그럼",
        "그런데": "근데",
        "따라서": "그래서",
        "하지만": "그렇지만",
    }

    return conjunction, alternative


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)
    conjunction, alt = load_conjunction()
    result = chg_word(test, conjunction, alt)
    print("Result: ", result)

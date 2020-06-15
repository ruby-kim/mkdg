"""
origin word.
komoran 형태소 분석기로 돌린 word값이 아닌,
순수 space 기준으로 나온 단어들
"""
from mkdg.utils.chgword import chg_word


def load_origin():
    from mkdg.utils.getmisspell import misspell_single_data
    """
    Load origin word data

    Returns: origin word dictionary
    """
    origin = misspell_single_data()
    return origin


if __name__ == "__main__":
    test = [
        "이태원 클럽발 확진자가 늘어났다.",
        "일 년 전이라도 여행 많이 가볼걸",
        "빨리 사태가 진정되었으면 좋겠다",
    ]

    print("Origin: ", test)
    origin = load_origin()
    result = chg_word(test, origin)
    print("Result: ", result)

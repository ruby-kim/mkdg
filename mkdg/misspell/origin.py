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
        "근데 그때도 바빴네 인생 무엇",
        "적어도 마스크 안끼고 회사 일하고 싶다",
        "이제 무슨말 쓰지",
        "생각보다 코드가 이것저것 많이 생겨난다",
        "한 발 짝 더 고인물이 된 느낌이다",
        "이젠 썩은물이 되게 해주세요",
    ]

    print("Origin: ", test)
    origin = load_origin()
    result = chg_word(test, origin)
    print("Result: ", result)

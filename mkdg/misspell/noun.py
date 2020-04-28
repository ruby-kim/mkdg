"""
명사
"""
from mkdg.utils.chgword import chg_word


def load_noun():
    noun = {
        "배달": [
            "배달",
            "배다", "베달",
        ],
        "카드": [
            "카드",
            "커드", "캬드",
        ],
        "세트": [
            "세트",
            "세뜨", "셋트","셋뜨",
        ],
        "주문": [
            "주문",
            "주뭄", "주뭉",
        ],
        "가능": [
            "가능",
            "카능", "카넝", "카느엉", "가느엉",
        ],
        "메뉴": [
            "메뉴",
            "마뉴"
        ],
        "얼마": [
            "얼마",
        ],
        "추가": [
            "추가",
            "츠가", "츄가",
        ],
        "예약": [
            "예약",
            "예악", "에약", "에악",
        ],
        "정도": [
            "정도",
            "정두"
        ],
        "결제": [
            "결제",
            "결재"
        ],
        "할인": [
            "할인",
            "활인",
        ]

    }

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

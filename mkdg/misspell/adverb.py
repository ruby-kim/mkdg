"""
부사
"""
from mkdg.utils.chgword import chg_word


adverb = {
    "좀": [
        "좀",
        "쫌",
    ],
    "더": [
        "떠",
    ],
    "많이": [
        "만이",
    ],
    "안": [
        "안",
        "앙",
    ],
    "따로": [
        "따로",
        "따루",
    ],
    "다": [
        "다",
        "따", "타",
    ],
    "잘": [
        "잘",
        "자알",
    ],
    "지금": [
        "지금",
        "직금", "작금",
    ],
    "혹시": [
        "혹시",
        "호옥시",
    ],
    "얼마나": [
        "얼마나",
        "얼만아",
    ]
}

alternative = {

}

if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)

    result = chg_word(test, adverb)  # , alternative)
    print("Result: ", result)

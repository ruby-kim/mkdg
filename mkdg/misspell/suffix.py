"""
접사\
"""
from mkdg.utils.chgword import chg_word


suffix = {
    "비": [
        "비",
        "삐",
    ],
    "제": [
        "제",
        "쩨",
    ],
    "불": [
        "불",
    ],
    "무": [
        "무",
        "무우",
    ],
    "생": [
        "생",
        "쌩",
    ],
    "초": [
        "초",
    ],
    "소": [
        "소",
    ],
    "반": [
        "반",
    ],
    "대": [
        "대",
    ],
    "신": [
        "신",
        "씬",
    ]
}

if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)
    result = chg_word(test, josa)  # , alternative)
    print("Result: ", result)

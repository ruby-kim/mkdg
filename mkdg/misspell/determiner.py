"""
관형사
"""
from mkdg.utils.chgword import chg_word


def load_determiner():
    determiner = {
        "네": [
            "네",
            "넴", "넹", "넷", "넵",
        ],
        "몇": [
            "몇",
            "몃",
        ],
        "한": [
            "한",
            "함",
        ],
        "어떤": [
            "어떤",
            "어딴", "어뜬",
        ],
        "두": [
            "두",
            "둘",
        ],
        "이": [
            "이",
        ],
        "그": [
            "그",
        ],
        "다른": [
            "다른",
            "",
        ],
        "이런": [
            "이런",
            "이론", "이른", "오런", "요런",
        ],
        "세": [
            "세",
        ]
    }

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
    result = chg_word(test, determiner)  # , alternative)
    print("Result: ", result)


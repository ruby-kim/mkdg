"""
형용사
"""
from mkdg.utils.chgword import chg_word


def load_adjective():
    adjective = {
        "없": [
            "없",
            "업"
        ],
        "어떻": [
            "어떻",
            "어떡",
        ],
        "맵": [
            "맵",
        ],
        "같": [
            "같",
            "갓", "갇",
        ],
        "맛있": [
            "맛있",
            "맛잇", "맜있", "맜잇",
        ],
        "괜찮": [
            "괜찮",
            "괜찬", "괞찮",
        ],
        "그렇": [
            "그렇",
            "그렿", "그럿",
        ],
        "다르": [
            "다르",
            "다른",
        ],
        "많": [
            "많",
            "만", "맣",
        ],
        "크": [
            "크",
            "큰",
        ],

    }

    alternative = {

    }

    return adjective, alternative


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)
    adjective, alt = load_adjective()
    result = chg_word(test, adjective)  # , alt)
    print("Result: ", result)

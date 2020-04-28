"""
어미
"""
from mkdg.utils.chgword import chg_word


def load_eomi():
    eomi = {
        "어요": [
            "어요",
            "엇요", "어용", "어욘",
        ],
        "고": [
            "고",
            "구",
        ],
        "면": [
            "면",
            "명",
        ],
        "아요": [
            "아요",
            "야요",
        ],
        "니다": [
            "니다", "습니다",
            "습다", "슴다", "슷니다", "숩다", "스비다",
            "숩니다", "슷니다", "습닛다",
            "니당", "닌다", "니단", "니담", "님당",
            "닛당", "님다", "닛다", "니닷",
        ],
        "어": [
            "어",
            "엇",
        ],
        "게": [
            "게",
        ],
        "에요": [
            "에요",
            "예요",
        ],
        "게요": [
            "게요",
        ],

    }

    alternative = {
        "습니다": "니다",
    }

    return eomi, alternative


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)
    eomi, alt = load_eomi()
    result = chg_word(test, eomi)  # , alt)
    print("Result: ", result)

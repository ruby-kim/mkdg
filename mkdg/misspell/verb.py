"""
동사
    * 니다: 습니다와 통합하여 사용
"""
from mkdg.utils.chgword import chg_word


verb = {
    "니다": [
        "니다",
        "습다", "슴다", "슷니다", "숩다", "스비다",
        "숩니다", "슷니다", "습닛다",
        "니당", "닌다", "니단", "니담", "님당"
    ],
}

alternative = {
    "습니다": "니다"
}


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]
    print("Origin: ", test)
    result = chg_word(test, verb, alternative)
    print("Result: ", result)

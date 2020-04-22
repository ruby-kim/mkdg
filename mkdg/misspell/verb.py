"""
동사
    * 니다: 습니다와 통합하여 사용
"""
import random
import re


verb = {
    "니다": [
        "니다",
        "습다", "슴다", "슷니다", "숩다", "스비다",
        "숩니다", "슷니다", "습닛다",
        "니당", "닌다", "니단", "니담", "님당"
    ],
}

if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)

    for i in range(len(test)):
        random.seed()
        test[i] = test[i].replace("습니다", "니다")
        for key, value in verb.items():
            check = [m.start() for m in re.finditer(key, test[i])]

            if len(check) is not 0:
                randChg = value[random.randint(0, len(value)-1)]
                test[i] = test[i].replace(key, randChg)

    print("Result: ", test)

"""
조사
    * 주격: 이, 가, 께서, 에서, 서
    * 서술격: 이다
    * 목적격: 을,를
    * 보격: 이, 가
    * 관형격: 의
    * 부사격: 에, 에서, 에게, 에게서, 한테, (으)로, 와, 과...
    * 호격: 아, 야
"""
from mkdg.utils.chgword import chg_word
from mkdg.utils.getmisspell import misspell_single_data


def load_josa():
    """
    Load josa data

    Returns: josa dictionary, alternative list
    """
    filename = "data/josa.csv"
    josa = misspell_single_data(filename)
    alternative = {

    }
    return josa, alternative


if __name__ == "__main__":
    test = [
        "오늘 코로나에 걸린 사람이 줄었습니다.",
        "많은 연구원들이 좋아할 것 입니다.",
        "병원 관계자들 또한 좋아할 것입니다."
    ]

    print("Origin: ", test)
    josa, alt = load_josa()
    result = chg_word(test, josa)  # , alt)
    print("Result: ", result)

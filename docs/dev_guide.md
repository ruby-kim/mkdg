# Development Guide
## 1. ```data/```
* 데이터와 관련된 파일들 저장
* 원본 소스는 올리지 말것(.gitignore 참고)
* python 파일 실행은 최상위에서(git clone 후 cd하면 바로 나오는 곳)
* 파일 목록
  * 원본파일: 20200404060046918.txt (사회 폴더 맨 위 파일)
  * user_dict.txt: 코모란 사용자 사전 ```추가하고 싶은 단어\n```
<br><br>
 
## 2. ```./misspell.py```
<br><br>

## 3. ```mkdg/option.py```
<br><br>

## 4. ```mkdg/misspell/```
* 명사, 동사, 부사 등 목록 리스트를 작성
* 기본 작성법
  ```python 
  # mkdg/misspell/____.py
  import random
  import re


  misspellList = {
            "원래 형태": [
                          "원래 형태",   # 극소수의 확률로 추출
                          "바꾸고 싶은 형태1", "바꾸고 싶은 형태2", "바꾸고 싶은 형태3", ...
            ],
            "원래 형태2: [
            ],
            ...
  }
    
  alternative = {
            "타겟 단어": "같은 취급을 해주고 싶은 단어"
            # "습니다": "니다"       # mkdg/misspell/verb.py 참고
  }
  ```
<br><br>

## 5. ```mkdg/utils/```
### 1) chgword.py
* 원본을 맞춤법이 틀린 단어들로 바꾸는 코드
* 개발 완료된 상태로, 기능 향상에 대해서 코드 수정 및 pull request 부탁드립니다.
<br><br>

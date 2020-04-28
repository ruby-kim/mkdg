# Development Guide
python 파일 실행은 최상위에서(git clone 후 cd하면 바로 나오는 곳) 진행해주세요.
<br>

## 1. ```data/```
* 데이터와 관련된 파일들 저장
* 원본 소스는 올리지 말것(.gitignore 참고)
* 파일 목록
  * 전처리 된, 문법을 틀리게 하고 싶은 .txt 파일 넣기
  * user_dict.txt: 코모란 사용자 사전 ```추가하고 싶은 단어\n```
<br><br>
 
## 2. ```./misspell.py```
* 실행 시 ```data/```폴더의 특정 데이터를 문법오류가 있는 데이터로 변경 후 ```data/tgt/```폴더에 저장
<br><br>

## 3. ```mkdg/option.py```
* ```./misspell.py```을 실행했을 시, [filename]에 관한 옵션 설정
* 현재 비활성화 되어 있음
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

### 2) frequency.py
* 원본.txt에서 사용된 단어의 빈도수를 tag별로 내림차순으로 출력(기본값: 30개)
* tag: 형용사, 부사, 접속사, 관형사, 어미, 조사, 명사, 선어말어미, 접사, 동사
<br><br>

### 3) getmisspell.py
* 원본.txt에서 추출된 tag별 값을 불러온 후 저장
* tag: 형용사, 부사, 접속사, 관형사, 어미, 조사, 명사, 선어말어미, 접사, 동사
<br><br>

### 4) loadfile.py
* 원본.txt의 내용을 추출함
* 현재까지 .txt에 대한 처리만 진행
<br><br>

### 5) preprocess.py
* 원본.txt에서 komoran 사용 후 전처리 시키는 코드
<br><br>

### 6) writefile.py
* 결과.txt의 내용을 저장함
* 현재까지 .txt에 대한 처리만 진행
<br><br>
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
* ```data/misspell.xlsx```에서 타겟단어 및 변경할 형태 작성
* sheet 종류: adjective(형용사), adverb(부사), conjunction(접속사), determiner(관형사), eomi(어미), josa(조사), noun(명사), preEomi(선어말어미), suffix(접사), verb(동사)
* 기본 작성법: 해당 sheet를 선택 후, 아래와 같이 수정해주세요.<br>
  |origin|change 1|change 2| ... |
  |:--:|:--:|:--:|:--:|
  |원래 단어1|변경할 형태1|변경할 형태 2|...|
  |원래 단어2|변경할 형태1|변경할 형태 2|...|
<br><br>

## 5. ```mkdg/utils/```
### 1) chgword.py
* 원본을 맞춤법이 틀린 단어들로 바꾸는 코드
* 개발 완료된 상태로, 기능 향상에 대해서 코드 수정 및 pull request 부탁드립니다.
<br><br>

### 2) frequency.py
* ```data/원본.txt```에서 사용된 단어의 빈도수를 tag별로 내림차순으로 출력(기본값: 30개)
* tag: 형용사, 부사, 접속사, 관형사, 어미, 조사, 명사, 선어말어미, 접사, 동사
<br><br>

### 3) getmisspell.py
* ```data/misspell.xlsx```에서 추출된 tag별 값들을 모두 불러온 후 저장
* tag: 형용사, 부사, 접속사, 관형사, 어미, 조사, 명사, 선어말어미, 접사, 동사
<br><br>

### 4) loadfile.py
* ```원본.txt```와 ```misspell.xlsx```의 내용을 추출함
* 원본은 ```.txt```, 태그는 ```.xlsx``` 확장명 사용
<br><br>

### 5) preprocess.py
* ```data/원본.txt```에서 komoran 사용 후 전처리 시키는 코드
<br><br>

### 6) writefile.py
* ```결과.txt```의 내용을 저장함 (최종: ```data/tgt/결과.txt```)
* 현재 .txt에 대한 처리만 진행
<br><br>
# Development Guide
python 파일 실행은 최상위에서(git clone 후 cd하면 바로 나오는 곳) 진행해주세요.
<br>

## 1. ```data/```
* 데이터와 관련된 파일들 저장
* 전처리 된, 문법을 틀리게 하고 싶은 .txt 파일 넣기
* 원본 소스는 올리지 말것(.gitignore 참고)

### 1) ```data/user_dict.txt```
* 코모란 사용자 사전
* 나무, 친구 등 명사로 취급해야 하는 단어가 '나','무' / '친','구' 등의 형태로 분리되어서 나올 때 해당 단어 추가<br>```추가하고 싶은 단어    형태소종류\n```
<br><br>

### 2) ```data/misspell.xlsx```
* 타겟단어(원래형태) 및 변경할 형태 작성
* sheet 종류: adjective(형용사), adverb(부사), conjunction(접속사), determiner(관형사), eomi(어미), josa(조사), noun(명사), preEomi(선어말어미), suffix(접사), verb(동사)  [[참고사이트]](https://docs.komoran.kr/firststep/postypes.html)
* 기본 작성법: 해당 sheet를 선택 후, 아래와 같이 수정해주세요.<br>
  |origin|change 1|change 2| ... |
  |:--:|:--:|:--:|:--:|
  |원래 단어1|변경할 형태1|변경할 형태 2|...|
  |원래 단어2|변경할 형태1|변경할 형태 2|...|
* 기본적으로 행의 **change ~**는 10번까지 존재합니다. 변경할 형태가 10개가 넘어도 코드는 정상적으로 작동되니 마음껏 추가하세요.
<br><br>

## 2. ```./misspell.py```
* 실행 시 ```data/```폴더의 특정 데이터를 문법오류가 있는 데이터로 변경 후 ```data/tgt/```폴더에 저장
<br><br>

## 3. ```mkdg/option.py```
* ```./misspell.py```을 실행했을 시, [filename]에 관한 옵션 설정
* 현재 비활성화 되어 있음
<br><br>

## 4. ```mkdg/misspell/```
* ```data/misspell.xlsx```에서 작성된 목록을 불러온 후 데이터프레임화
* 기본 작성법은 아래와 같습니다. (아래의 파일은 ```mkdg/misspell/adjective.py```의 일부입니다)
  ```python
  def load_adjective():
      from mkdg.utils.getmisspell import misspell_single_data
      
      adjective = misspell_single_data("adjective")
      alternative = {
          "똑같은 취급을 해주고 싶은 단어1": "원래 단어1",
          "뜩같은 취급을 해주고 싶은 단어2": "원래 단어2",
          ...
      }
      return adjective, alternative
  ```
* 만약 alternative를 작성했다면, "똑같은 취급을 해주고 싶은 단어"를 ```data/misspell.xlsx```에서 해당하는 sheet로 이동 후 **change**항목에 작성해주세요.<br>
  예를 들어<br>
  ```python
  # mkdg/misspell/eomi.py
  alternative = {
      "습니다": "니다",
  }
  ```
  라고 작성했다면, 여기서 "똑같은 취급을 해주고 싶은 단어"=>"습니다" / "원래 단어"=>"니다"가 됩니다.<br>
  그러면 ```data/misspell.xlsx```에서 sheet가 eomi인 곳으로 이동 후, 다음과 같이 표를 구성합니다.<br>
  |origin|change 1| ... |
  |:--:|:--:|:--:|
  |니다|습니다|...|

<br><br>

## 5. ```mkdg/utils/```
### 1) chgword.py
* 원본을 맞춤법이 틀린 단어들로 바꾸는 코드
* 변경 후 원본 그대로 나올 확률은 1/n
  ```
  origin: 안녕하세요
  change: 안녕, 안뇽, 앙녕, 안녀영
  
  이라고 있을 시,
  '안녕하세요'를 변경하여 다시 '안녕하세요'가 나올 확률은 1/5
  다른 단어들 또한 1/5 확률로 랜덤 변경
  ```
* 개발 완료된 상태로, 기능 향상에 대해서 코드 수정 및 pull request 부탁드립니다.
<br><br>

### 2) analyze.py
* ```data/원본.txt```파일 분석
* tag: 형용사, 부사, 접속사, 관형사, 어미, 조사, 명사, 선어말어미, 접사, 동사
* 사용법은 235~245번째 줄의 analyze 함수 참고
1. print_len: ```data/원본.txt```의 문장 수 출력
2. print_origin_frequency: ```data/원본.txt```를 띄어쓰기 기준으로 단어 생성 후, 해당 값의 빈도수를 내림차순으로 모두 출력
3. judge_tag: ```data/원본.txt```의 문장별 형태소 분석 후, 각 단어의 tag 판별
4. print_morph: 원본의 형태소 분석 결과(텍스트) 출력
5. print_pos: 원본의 형태소 분석 결과(텍스트, 태그) 출력
6. print_tag_frequency: tag 별 사용된 단어의 빈도수를 내림차순으로 출력(기본값: 30개)
7. print_dict: 인자로 들어가는 tag 값의 리스트 출력
8. save_compare("morph"): 4번의 ```print_morph```의 값을 ```data/analyze/원본_morph.txt``` 에 저장
9. save_compare("pos"): 5번의 ```print_pos```의 값을 ```data/analyze/원본_pos.txt```에 저장
10. save_origin_frequency: 2번의 ```print_origin_frequency```의 값을 ```data/analyze/원본_origin.txt```에 저장
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
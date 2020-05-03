# Misspelled-Korean-Data-Generator
맞춤법이 틀린 한국어 데이터를 만드는 코드
<br><br>

## Requirements
* konlpy
  ```bash
  pip install konlpy
  ```
* pandas
  ```bash
  pip install pandas
  ```
<br>

## Installation
```bash
git clone https://github.com/study-ai-data/mkdg
cd mkdg
python setup.py install
```
<br>

## Getting Started
1. 원본 파일을 ```./data``` 폴더에 넣어주세요. (없을 시 폴더 생성)
2. ```./misspell.py```에서 18번 째 줄의 ```filename = "A 음식점(15,726)_only_speak.txt"```을 원하는 파일 이름으로 변경해주세요.
3. 코드를 실행 시 문법오류가 있는 데이터가 ```./data/tgt/``` 폴더에 .txt 형태로 저장됩니다.
   ```bash
   python misspell.py
   ```
<br>

## Note
자료의 부족으로 아직은 직접 데이터를 분석해서 데이터를 생성해야 합니다.<br>
데이터 분석은 [[docs/dev_guide]](https://github.com/study-ai-data/mkdg/blob/master/docs/dev_guide.md)를 참고해주세요.
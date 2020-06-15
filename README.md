# Misspelled-Korean-Data-Generator
맞춤법이 틀린 한국어 데이터를 만드는 코드
<br><br>

## Requirements
원래 ```requirements.txt```로 한번에 설치하게 하려고 했는데, 패키지 중 ```py-hanspell```자체 내에서 설치 오류가 발생하여 ```py-hanspell```만 따로 설치 방법을 적습니다.
<br>이후에 업데이트 되어서 코드가 정상적으로 잘 작동하면 ```requirements.txt```에 추가하도록 하겠습니다.<br>
(참고) 200615: py-hanspell이 곧 업데이트 예정 중이라고 함. 입데이트가 완료될 시 requirements.txt에 삽입할 예정임
* ```py-hanspell``` 설치법
  ```bash
  git clone https://github.com/study-ai-data/py-hanspell
  cd py-hanspell
  python setup.py install
  ```
* ```py-hanspell```을 제외한 나머지 패키지 설치:
  ```bash
  pip install -r requirements.txt
  ```

## Installation
```bash
python setup.py install             # install package
```
<br>

## Getting Started
1. 원본 파일을 ```./data``` 폴더에 넣어주세요. (없을 시 폴더 생성)
2. ```./misspell.py```에서 53번 째 줄의 ```filename = "A 음식점(15,726)_only_speak.txt"```을 원하는 파일 이름으로 변경해주세요.
3. 코드를 실행 시 문법오류가 있는 데이터가 ```./data/tgt/``` 폴더에 .txt 형태로 저장됩니다.
   ```bash
   python misspell.py
   ```
<br>

## Note
자료의 부족으로 아직은 직접 데이터를 분석해서 데이터를 생성해야 합니다.<br>
데이터 분석은 [[docs/dev_guide]](https://github.com/study-ai-data/mkdg/blob/master/docs/dev_guide.md)를 참고해주세요.

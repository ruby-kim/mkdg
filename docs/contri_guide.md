# Contributor Guide
임의로 작성<br>
last update: 2020-04-22
<br>

## 1. Commit 메시지
* 제목과 본문을 한 줄 띄워 분리
* 제목 작성 시 아래를 참고해서 작성
    1. ```영어```로 작성
    2. 제목은 50자 이내로
    3. 제목 첫 글자는 대문자로
    4. 제목 끝에 ```.```금지
* 본문 작성 시 아래를 참고해서 작성
  1. ```영어```, ```한국어``` 중 선택해서 작성
  2. ```어떻게```보다 ```무엇을```, ```왜```에 맞춰 작성
  3. 각 내용마다 구분이 가도록 작성(order & unorder 사용)

<br>

## 2. Branch 이름
## 3. 변수 작성 방법
## 4. 함수 작성 방법
## 5. 버전 표기 기준
## 6. Merge 규칙
* 각자 맡은 코드를 작성 및 수정 후,<br>
팀원은 Pull request에 있는 해당 Issue를 보고 피드백 남기기<br>
(merge 찬성 혹은 개선 내용 추가)
<br>

## 7. Issue 규칙
## 8. Wiki 규칙
## 9. 실행방법
* setting
```bash
git clone https://github.com/study-artificial-intelligence/mkdg.git
cd mkdg
python setup.py install
```
이후에 실행이 안될 시 python path에 해당 경로 추가
* running
```bash
python misspell.py # --filename [filename1] [filename2]
```
filename: 원하는 파일 이름. 개수 제한은 없지만, 1개 이상은 입력 필수.<br>
현재 파일이름 입력 시 실행되는 기능은 지원하지 않음

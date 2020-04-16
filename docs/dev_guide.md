# Development Guide
채워지지 않은 부분은 의논이 필요함<br>
last update: 2020-04-16 ::
<br>

## 1. Commit 메시지
* 제목과 본문을 한 줄 띄워 분리
* 제목 작성 시 아래를 참고해서 작성
    1. ```영어```로 작성
    2. 제목은 50자 이내로
    3. 제목 첫 글자는 대문자로
    4. 변경 종류
       * [Add]: 파일 내용 추가(본문 작성 **필수**)
       * [Modify]: 파일 내용 수정(본문 작성 **필수**)
       * [Del]: 파일 내용 삭제(본문 작성 **필수**)
       * [New]: 파일 생성(본문 작성 **필수**)
       * [Remove]: 파일 삭제(본문 작성 **선택**)
    5. 파일명
       * 패키지(폴더)/파일명
    6. 제목 끝에 ```.```금지
* 본문 작성 시 아래를 참고해서 작성
  1. ```영어```, ```한국어``` 중 선택해서 작성
  2. ```어떻게```보다 ```무엇을```, ```왜```에 맞춰 작성
  3. 각 내용마다 번호 붙여 작성
  4. 될 수 있으면 def 기준으로 작성
* 예시
  1. mkdg/__init__.py에 내용 추가: 
     ```bash
     [Add] mkdg/__init__.py
     package import 문법 작성
     ```
  2. mkdg/option.py 파일 생성:
     ```bash
     [New] mkdg/option.py
     1. setting_parse: 파일이름 입력 옵션 선택 및 파싱
     ```
  3. setup.py 파일 삭제:
     ```bash
     [Remove] setup.py
     ```
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
  python main.py --filename [filename1] [filename2]
  ```
  * filename: 원하는 파일 이름. 개수 제한은 없지만, 1개 이상은 입력 필수
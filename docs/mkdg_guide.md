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

## 4. ```mkdg/loader```
<br><br>

## 5. ```mkdg/misspell```
* 기본 작성법은 다음과 같다.
  ```python 
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

  if __name__ == "__main__":
      test = [
          "예시 문장 1",
          "예시 문장 2",
          ...
      ]

      print("Origin: ", test)  # 원래 문장들 출력
 
      for i in range(len(test)):
          random.seed()  # 랜덤 시드 생성
  
          # 습니다-니다 같이 애매한 경우(integrate. mkdg/misspell/verb.py 참고)
          # test[i] = test[i].replace("습니다", "니다")  
  
          for key, value in verb.items():
              # 각 [예시 문장]에서 [원래 형태] 위치들을 저장
              check = [m.start() for m in re.finditer(key, test[i])]

              # 문장 내에 [원래 형태]가 존재할 시, [바꾸고 싶은 형태]로 랜덤 뽑기 및 변환
              if len(check) is not 0:
                  randChg = value[random.randint(0, len(value)-1)]
                  test[i] = test[i].replace(key, randChg)

      print("Result: ", test) # 변경된 문장들 출력
  ```
<br><br>

## 6. ```mkdg/utils```
<br><br>

## 7. ```mkdg/writer```

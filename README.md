# python 문법

문자열은 ' " '''로 감싸서 사용

### 입력

- c언어에서의 scanf
- 사용자의 입력을 받음
- string으로 입력을 받는다

```python
  input()
```

- input함수에 문자열을 넘겨주면 입력을 받을 때 가이드로 출력된다

### 변수

- 값을 저장하는 메모리 공간
- 값을 저장하기 위해 사용
- 변수명은 숫자, 영문으로 작성한다

  - 숫자로 시작하거나 숫자로만 이루어진 변수명은 오류를 발생 시킨다
  - 띄어쓰기는 언더바(\_)를 사용하여 구분
  - 대소문자를 구분한다
  - 예약어는 변수명으로 사용할 수 없다

- c와 달리 변수 선언시 자료형을 명시하지 않는다

  ```python
  a = 100
  b = 'python'
  ```

### / 연산자

- / 연산을 진행한 값을 애 float이다

### print

- "+", "," 를 이용하여 자료형이 다른 값을 연결해 출력할 수 있다
  - +는 문자열을 띄어쓰기 없이 연결
  - ,는 문자열을 띄어쓰기를 추가하여 연결

### int함수

- 입력 받은 값을 정수로 타입 변경을 한다
  ```python
  int('123') --> 123
  int('12.3') --> 12
  ```

### 연산자

| 연산자 |      의미      |
| :----: | :------------: |
|   /    | 나눈 값(float) |
|   //   | 나눈 몫(정수)  |
|   %    |     나머지     |
|  \*\*  |      제곱      |

### 대입연산자

- 대입연산자의 우측 연산이 끝난 후 좌측에 대입된다

  - 변수와 변수의 연산, 변수와 값에 연산, 값과 값이 모두 연산 가능하다
  - 대입된 변수는 새로운 값으로 덮어 씌어진다
  - 대입연산자에 왼쪽이 변수가 아니라면 오류 발생
  - 대입연산자의 왼쪽애는 한개의 변수가 존재해야 한다
  - 여러개의 값을 한번에 대입 가능하다

    - 좌우 값의 갯수가 같아야 한다

      ```python
      a, b = 100, 200
      # a = 100
      # b = 200
      ```

      에러 코드

      ```python
      num1, num2 = 100, 200
      num1, num2 = 100
      num = 100, 200 # 에러는 발생 X
      ```

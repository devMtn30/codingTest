#각 자리가 숫자(0~9) 로만 이루어진 무자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 x 혹은 +연산자만 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

#+보다 x를 먼저 계산하는 일반적인 계산과 달리 모든 계산은 왼쪽부터 순서대로 이뤄진다고 가정

#02984라는 문자열로 만들 수 있는 가장 큰 수는 (((0+2)x9)x8)x4 = 576이다.
#만들어질 수 있는 가장 큰 수는 항상 20억 이하의 정수

#입력조건 : 첫째 줄에 여러개의 숫자로 구성된 하나의 문자열 S가 주어진다. 1이상 20이하

#출력조건 : 첫째 줄에 만들어 질 수 있는 가장 큰수를 출력

#입력예시 : 02984   출력 : 576
#입력예시 : 567     출력 : 210


#1. 데이터 받기
str = input()
result = 0
n = int(str[0]) 

if int(str[0]) == 0:
  n = int(str[1])

#4.반복
for i in range(1,len(str)):
  #2. 배열의 n번과 n+1을 비교하여 연산
  if str[i] != 0:
    n *= int(str[i])

print(n)

  
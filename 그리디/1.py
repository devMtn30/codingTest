
# 프로그램 소스코드
#문제 : 음식점 계산문제 거스름돈 500,100,50,10원 동전
#손님에게 거슬러줘야 할 돈 N원일때, 거슬러 줘야하는 동전의 최소개수 구하기

coin = [500,100,50,10]
n = int(input("거스름돈 입력:"))
result = 0
for ncoin in coin:
   result += n // ncoin
   n = n% ncoin
print(result)
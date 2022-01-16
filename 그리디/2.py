#문제 N 1이상 10만이하 K는 2이상 10만 이하가 공백을 기준으로 자연수로 주어질때 N이 1이 될떄까지 두가지의 과정중 하나를 반복적 수행

#1.N에서 1을 뺀다.
#2.N을 K로 나눈다.

#이떄 1번 혹은 2번의 과정을 수행하는 최소 횟수를 구하는 프로그램

n, k = map(int, input().split())

result = 0

while True:
  target = (n//k) *k
  result += (n-target)
  n = target

  if n < k:
    break;

  result +=1
  n //= k

result+=(n-1)
print(result)
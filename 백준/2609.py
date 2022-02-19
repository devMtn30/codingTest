# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

def gcd(a,b):
  if a % b == 0:
    return b
  r = a % b
  return gcd(b,r)
  
A,B = map(int,input().split())
if A > B:
  gcdiv = gcd(A,B)
elif B > A:
  gcdiv = gcd(B,A)
else:
  gcdiv = A

print(gcdiv)
print(int(A*B/gcdiv))
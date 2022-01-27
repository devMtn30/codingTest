#num1,num2 = map(int,input().split())


numbers = []
result = []
result1 = ""

N,X = input().split()
numbers = input().split()

for num in numbers:
  if int(num) < int(X):
    result.append(num)
print(' '.join(result))


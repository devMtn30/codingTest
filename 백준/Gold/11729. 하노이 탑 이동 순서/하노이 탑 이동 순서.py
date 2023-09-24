N = int(input())

def hanoi(n,a,b,c):
  if n == 1:
    print(a,c)
    return
  hanoi(n-1,a,c,b)
  print(a,c)
  hanoi(n-1,b,a,c)
print((2**N)-1)
hanoi(N,1,2,3)
import sys

N = int(sys.stdin.readline().rstrip())
gx = 0
for i in range(1,N+1):
    gx += (N//i)*i
print(gx)

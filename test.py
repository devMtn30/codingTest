N = int(input())
cal = 1
i = 1
while N > cal:
  if N == 1:
    i = 0
    break;
  cal += 6*i
  i+=1

print(i) 
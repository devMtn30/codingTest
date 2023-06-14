min_val = 999
total = 0
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
       total += num
       if min_val > num:
            min_val = num
            
if total != 0:
    print(total)
    print(min_val)
else:
    print(-1)

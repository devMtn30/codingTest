day = int(input())
car_num_list = list(map(int, input().split()))

result = 0

for i in car_num_list:
    if day == i:
        result+=1

print(result)


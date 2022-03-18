N = int(input())
arr = sorted(list(map(int, input().split())), reverse=True)

if N == 1:
    print(arr[0]**2)
else:
    print(arr[0]*arr[len(arr)-1])
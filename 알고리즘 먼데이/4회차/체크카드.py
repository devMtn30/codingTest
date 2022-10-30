from collections import deque

que = deque()

account, N = map(int, input().split())
temp = 0
for i in range(N):
    command, money = map(str, input().split())
    if command == "deposit":
        account += int(money)
    if temp != 0 and account >= temp:
        account += -temp
        temp = 0
    if len(que) != 0 and temp == 0:
        temp = que.popleft()
    if (command == "pay" or command == "reservation") and account >= int(money):
        account += -int(money)
    if command == "reservation" and account < int(money):
        que.append(int(money))
print(account)


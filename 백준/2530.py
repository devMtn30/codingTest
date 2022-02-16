hour, minute, sec = map(int, input().split())
ctime = int(input())

if sec+ctime >= 60:
  minute += (sec+ctime) //60
  sec = (sec+ctime) % 60
  if minute >= 60:
    hour += minute // 60
    minute = minute % 60
  if hour >= 24:
    hour = hour % 24
else:
  sec += ctime
print(f"{hour} {minute} {sec}")
import time
#참고코드

n = int(input())
x, y = 1,1
plans = input().split()

start_time = time.time() # 측정 시작
#L,R,U,D에 따른 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U',"D"]

#이동 계획을 하나씩 확인하기
for plan in plans:
  #이동 후 좌표 구하기
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = y+dx[i]
      ny = y+dy[i]

  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue

  x,y = nx, ny

print(x,y)
end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력

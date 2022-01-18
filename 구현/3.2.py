# 행복 왕국의 왕실 정원은 체스판과 같은 8 * 8 좌표 평면
# 왕실 정원의 특정한 한칸에 나이트가 서있다.
# 나이트는 말을 타고 있어서 갈지자 형태로만 이동가능 정원 밖은 이동 불가
# 나이트는 2가지의 경우로 이동 가능하다
# 1.수평으로 두칸 이동한 후 수직 한칸 이동
# 2.수직으로 두칸 이동한 후 수평 한칸 이동
# 행의 위치는 1~8  열의 위치는 a~h(8가지) 

# 입력 조건 : 첫째 줄에는 8 * 8 좌표 평면상에서 현재 나이트가 위치한 곳의 좌표를 나타내는 두 문자로 구성된 열이 입력된다. 입력 문자는 a1처럼 행렬로 이뤄진다.

# 출력 조건 : 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하시오.


input = list(input())
convStr = ['a','b','c','d','e','f','g','h']
cnt = 0 

#매핑
for idx,_str in enumerate(convStr):
  if input[0] == _str:
    cnt = idx

#현재 위치 구하기
now= [cnt,int(input[1])]

#적용
col = now[0]
row = now[1]

#움직일 수 있는 경우의 수
movetype= [[1,2],[1,-2],[2,1],[2,-1],[-1,2],[-1,-2],[-2,1],[-2,-1]]
moveCnt = 0
for i in movetype:
  row = now[0]+i[0]
  col = now[1]+i[1]
  if row > 0 and row <= 8 and col > 0 and col <= 8:
    moveCnt+=1

print(moveCnt)



#배열에는 값 복사 후 초기화가 안되고 계속해서 더해진다. call by reffence
#(수정) Call by assignment이다. 즉 immutable 한 포맷의 객체(tuple 등)는 변경할 수 없지만, mutable한 포맷의 객체(list, dictionary, 직접 만든 클래스 등)는 변경할 수 있다는 특성을 갖는다.
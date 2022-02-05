# 문제
# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

# 입력
# 첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

# 출력
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

N = int(input())
cnt = 0
for i in range(1,N+1):
  if i < 100 :
    cnt +=1
    continue
  dif = int(str(i)[1]) - int(str(i)[0])
  pre_num = int(str(i)[0])
  flag = False
  for j in range(1,len(str(i))):
    now_num = int(str(i)[j])
    #다음 숫자랑 비교
    if now_num - pre_num != dif:
      flag =False
      break;

    pre_num = now_num
    flag = True
  if flag:
    cnt+=1
print(cnt)


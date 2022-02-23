def quickSort(data,start,end):
  if start >= end: #원소가 1개인 경우
    return

  key = start #키는 첫번째 원소
  i = start+1#왼쪽에서 출발
  j = end#오른쪽에서 출발
  
  while i <= j:#엇갈릴때까지 반복
    while data[i] <= data[key]:#키값보다 큰 값을 만날떄까지 오른쪽으로 이동
      i+=1
    while data[j] >= data[key] and j > start:#키값보다 작은 값을 만날떄까지
      j-=1
    if i > j : #현재 엇갈린 상태면 키값과 교체
      data[j] , data[key] = data[key], data[j]
    else: #엇갈리지 않았으면 큰값과 작은값을 교체
      data[j], data[i] = data[i], data[j]

  quickSort(data,start,j-1)
  quickSort(data,j+1,end)

data = [1,4,3,5,10,6,2,7,9,8]
quickSort(data,0,9)
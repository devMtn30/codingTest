def my_func(i,j,for_cnt,cnt):
  for x in range(for_cnt):
    if for_cnt//2 == 1:
      i+=1
      j-=1
    cnt+=1
    if cnt == X:
      return [i,j,cnt,'end']
  return [i,j,cnt,'not']

X = int(input())

i=1
j=1
cnt = 0
for_cnt = 0
flag = True
while True:
  if X == 1:
    print("1/1")
    break;

    
  cnt +=1
  
  if flag and not cnt == 1:
    j+=1
    flag=False
  elif flag==False and not cnt ==1:
    i+=1
    flag=True
  
  a = my_func(i,j,for_cnt,cnt)
  i = a[0]
  j = a[1]
  cnt = a[2]
  if a[3] == 'end':
    break;
    
  for_cnt+=1
    
print(i,j)



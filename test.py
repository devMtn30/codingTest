N = int(input())
cyclenum2 = 0
cyclenum = N
cnt=0
while True:
  if int(cyclenum) < 10 :
    fnum = 0
    bnum = N
  else :
    fnum = int(str(cyclenum)[0])
    bnum = int(str(cyclenum)[1])
  
  cyclenum = int(str(bnum)+str(fnum+bnum)[-1:])
  if cyclenum == cyclenum2:
    break;
  cyclenum2 = cyclenum
  print(cyclenum,cyclenum2)
  cnt+=1
  if int(cyclenum) == N:
    break;
  
print(cnt)
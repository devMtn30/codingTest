a1,a2,a3 = map(int,input().split())

money = 0
if a1 == a2 == a3:
  money = 10000+a1*1000
elif a1 == a2:
  money = 1000+a1*100
elif a2==a3 :
  money = 1000+a2*100
elif a3==a1 :
  money = 1000+a3*100
else:
  money = max(a1,a2,a3)*100


print(money)

  
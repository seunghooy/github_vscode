A, B = map(int,input().split())
if B-45 >= 0:
  print(A, B-45)
elif B-45 < 0 and A!=0:
  print(A-1,B+15)
else:
  print(23, B+15)
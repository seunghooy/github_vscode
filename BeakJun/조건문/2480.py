A, B, C = map(int,input().split())
max_value = max(A, B, C)

if A==B==C:
  print(10000+max_value*1000)
elif A==B:
  print(1000+A*100)
elif B==C:
  print(1000+B*100)
elif C==A:
  print(1000+100*A)
else:
  print(max_value*100)
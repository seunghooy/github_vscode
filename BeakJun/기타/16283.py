a, b, n, w = map(int, input().split())

count = 0

for i in range(1,n):
  A = i
  B = n-i
  if A*a + B*b == w:
    s = A
    g = B
    count += 1

if count ==1:
  print(s,g)
else:
  print("-1")
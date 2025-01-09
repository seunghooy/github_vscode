N = int(input())
A = str()
B = str()
for i in range(N):
  A[i], B[i] = map(str,input().split())

for i in range(N):
  print(int(A[i])+int(B[i]))
N, M = map(int,input().split())
A = [[]]
B = [[]]

for i in range(N):
  for j in range(M):
    A[i][j] = input()

for i in range(N):
  for j in range(M):
    B[i][j] = input()

print(A+B)
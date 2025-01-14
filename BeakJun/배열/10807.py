N = int(input())
list = input().split()
#list = map(int,input().split())
#print(list)
A =int(input())
count = 0
for i in range(N):
  if int(list[i]) == A:
#  if list[i] == A:
    count += 1
print(count)
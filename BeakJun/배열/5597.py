my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
A = ()

for i in range(28):
  A = int(input())
  my_list.remove(A)

print(my_list[0], my_list[1])
from itertools import permutations
s,r = input().split()
p_list = list(permutations(s,int(r)))
p_list.sort()
for i in p_list:
    print(''.join(i))

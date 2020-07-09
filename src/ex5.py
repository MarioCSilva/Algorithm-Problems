from itertools import permutations 

towers = str(input("towers: "))

lst = []

for char in towers:
    if char!=" ":
        lst.append(int(char))
  
num=lst[0]
max_left=lst[1]
max_right=lst[2]

all_arranj = permutations(range(1, num+1))

final_count=0
for state in all_arranj:
    count_left=1
    count_right=1

    left = state[0]
    for i in range(1,num):
        if state[i] > left:
            left = state[i]
            count_left+=1

    right = state[num-1]
    for k in range(num-1, -1, -1):
        if state[k] > right:
            right = state[k]
            count_right+=1

    if count_left==max_left and count_right==max_right:
        final_count+=1

print(final_count)
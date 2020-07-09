from itertools import permutations 

# Data Handling...
towers = str(input("towers: "))

lst = []

for char in towers:
    if char!=" ":
        lst.append(int(char))
  
num=lst[0]
max_left=lst[1]
max_right=lst[2]

# Generate all possible arrangements
all_arranj = permutations(range(1, num+1))

# For each arrangement check left and right side
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

    # If they match the desired number add to the counter
    if count_left==max_left and count_right==max_right:
        final_count+=1

print(final_count)
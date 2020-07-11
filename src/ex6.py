numb = input("-> ")

lst = numb.split(" ")

k = int(lst[0])
m = int(lst[1])

rockets = 0

for i in range(1,m+1):
    rockets+=i

print(rockets)
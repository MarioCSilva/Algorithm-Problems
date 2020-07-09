n = int(input("n: "))
p = str(input("p: "))

lst = []

for char in p:
    if char!=" ":
        lst.append(char)

counter=0

#Bubble Sort
for i in range(n-1):
    for k in range(n-i-1):
        if lst[k] > lst[k+1]:
            x=lst[k]
            lst[k]=lst[k+1]
            lst[k+1] = x
            counter+=1

print(lst)
print(counter)
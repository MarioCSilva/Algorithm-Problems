import sys

n = int(input("n: "))
p = int(input("p: "))

for i in range(sys.maxsize):
    if i**n == p:
        print(i)
        break
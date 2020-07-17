import sys

def calcPower(lst, index=None):
    if index == None:
        index = 0

    if index<len(lst)-1:
        return lst[index]**calcPower(lst, index+1)
    else:
        return lst[index]

def findAllPowers(value, size=None):
    # Size of the current exponential tower
    if size == None:
        size = 0

    total = 0
    if value % 2 == 0:
        init = 2
    else:
        init = 3
    for i in range(init, 9585, 2):
        for t in range(2, 9585):
            cur = i**t
            if (cur > value and t == 2):
                if size > 1:
                    total += 1
                return total
            if (cur > value):
                break
            if cur == value:
                num = findAllPowers(t,size+1)
                total += num

    return total

str_input = input()

lst = str_input.split("^")
lst = [ int(x) for x in lst ]

value = calcPower(lst)

print(value)

print(findAllPowers(value))
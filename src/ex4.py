def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True


str_input = input()

lst = str_input.split(" ")

n = int(lst[0])
c = int(lst[1])

prime_lst = [1]
for i in range(1,n):
    if test_prime(i):
        prime_lst.append(i)

final_str = str(n) + " " + str(c) + ": "

if len(prime_lst)%2==0:
    c = 2*c

    if c > len(prime_lst):
        c = len(prime_lst)

    for i in range(len(prime_lst)//2-c//2,len(prime_lst)//2+c//2):
        final_str += str(prime_lst[i]) + " "
else:
    c = 2*c-1

    if c > len(prime_lst):
        c = len(prime_lst)
    
    for i in range((len(prime_lst)+1)//2-(c-1)//2-1, (len(prime_lst)+1)//2+(c-1)//2):
        final_str += str(prime_lst[i]) + " "

print(final_str)
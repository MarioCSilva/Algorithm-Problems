import math

def find_bin_equal(n, k):
    # Calculate the interval of possible numbers
    min_val = int(math.pow(2,n-1) + 1)
    max_val = int(math.pow(2,n) -1)
    
    # Find the first multiple of k
    for num in range(min_val, max_val+1):
        if num % k == 0:
            first_mult = num
            break
    
    if first_mult == None:
        return 0
    
    # Find all possibilities
    count = 0
    num_steps = (max_val - first_mult) // k
    for num in range(num_steps):
        binary = ( bin(first_mult)[2:] )
        number_0 = binary.count('0')
        number_1 = binary.count('1')

        if number_0 == number_1:
            count += 1

        first_mult += k

    return count

if __name__ == "__main__":
    str_input = input()

    lst = str_input.split(" ")

    n = int(lst[0])
    k = int(lst[1])

    num = find_bin_equal(n, k)

    print(num)
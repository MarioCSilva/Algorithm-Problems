import heapq

def find_median(lst):
    maxh = []
    minh = []

    for val in lst:
        # Initialize the data-structure and insert/push the 1st streaming value
        if not maxh and not minh:
            heapq.heappush(maxh,-val)
            median = float(val)
        elif maxh:
            # Insert/push the other streaming values
            if val >= -maxh[0]:
                heapq.heappush(minh,val)
            else:
                heapq.heappush(maxh,-val)

            # Calculate the median
            if len(maxh)==len(minh):
                median = float(-maxh[0]+minh[0])/2
            elif len(maxh)==len(minh)+1:
                median = float(-maxh[0])
            elif len(minh)==len(maxh)+1:
                median = float(minh[0])

            # If min-heap and max-heap grow unbalanced we rebalance them by
            # removing/popping one element from a heap and inserting/pushing
            # it into the other heap, then we calculate the median
            elif len(minh)==len(maxh)+2:
                heapq.heappush(maxh,-heapq.heappop(minh))
                median = float(-maxh[0]+minh[0])/2
            elif len(maxh)==len(minh)+2:
                heapq.heappush(minh,-heapq.heappop(maxh))
                median = float(-maxh[0]+minh[0])/2
    return median


if __name__ == "__main__":
    str_input = input()

    lst = str_input.split(" ")

    lst = [ int(x) for x in lst ]

    median = find_median(lst)

    print(median)
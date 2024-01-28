# 1.1 You want to go up a flight of stairs that has n steps. You can either take 1
# or 2 steps each time. How many different ways can you go up this flight of
# stairs? Write a function count_stair_ways that solves this problem. Assume
# n is positive.

def count_stair_ways(n):
    """
    >>>count_stair_ways()
    """

    # 1 = 1

    # 2 = 1 + 1
    # 2 = 2

    # 3 = 2 + 1
    # 3 = 1 + 2
    # 3 = 1 + 1 + 1

    # 4 = 1 + 1 + 1 + 1
    # 4 = 2 + 2
    # 4 = 2 + 1 + 1
    # 4 = 1 + 1 + 2
    # 4 = 1 + 2 + 1

    # 5 = 1 + 1 + 1 + 1 + 1
    # 5 = 2 + 2 + 1
    # 5 = 2 + 1 + 2
    # 5 = 1 + 2 + 2
    # 5 = 1 + 1 + 2 + 1
    # 5 = 1 + 1 + 2 + 1
    # 5 = 2 + 1 + 1 + 1
    # 5 = 1 + 2 + 1 + 1
    
    # no more steps required

    #ways = 0
    # def count(n):
    # if n == 1:
    #     return 1
    # elif n == 2:
    #     return 2
    # else:
    #     return count_stair_ways(n - 1) + count_stair_ways(n - 2)

    if n == 0:
        return 1
    elif n == 1:
        return 1
    return count_stair_ways(n-1) + count_stair_ways(n-2)

# 2.2 Tutorial: Write a function that takes a list s and returns a new list
# that keeps only the even-indexed elements of s and multiplies them by their
# corresponding index.

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    # both solutions work
    # return [e * s.index(e) for e in s[0::2]]
    return [s[i] * i for i in range(0, len(s), 2)]

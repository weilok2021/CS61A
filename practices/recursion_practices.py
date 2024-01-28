# Easy
# Q1: In sum...
# Write a function sum that takes a single argument n and computes the sum of all integers between 0 and n inclusive. Assume n is non-negative.

def sum(n):
    """Computes the sum of all integers between 1 and n, inclusive.
    Assume n is positive.

    >>> sum(1)
    1
    >>> sum(5)  # 1 + 2 + 3 + 4 + 5
    15
    """

    if n == 1:
        return n
    return sum(n - 1) + n

def countdown_up(n):
    """Starts at n and simultaneously prints out the countdown from n to 0
    and the countup from n to 2*n, inclusive.

    >>> countdown_up(0)
    0

    >>> countdown_up(5)
    5
    4
    6
    3
    7
    2
    8
    1
    9
    0
    10
    """

    def count(x, y):
        # print the first n (only print once)            
        if x == 0 and y == 2 * n:
            print(x)
            print(y)
            return
        else:
            print(x)
            print(y)
            count(x - 1, y + 1)

    print(n)        
    count(n - 1, n + 1)
    
        
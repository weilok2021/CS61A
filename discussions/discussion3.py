# Recursion
# 1.1 Write a function that takes two numbers m and n and returns their product.
# Assume m and n are positive integers. Use recursion, not mul or *!
def multiply(m, n):
    if n == 1:
        return m
    else:
        return multiply(m, n - 1) + m

# 1.3 Tutorial: Recall the hailstone function from Homework 1. First, pick
# a positive integer n as the start. If n is even, divide it by 2. If n is odd,
# multiply it by 3 and add 1. Repeat this process until n is 1. Write a recursive
# version of hailstone that prints out the values of the sequence and returns
# the number of steps.
# Hint: When taking the recursive leap of faith, consider both the return value
# and side effect of this function.

def hailstone(n):

    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print("side effect", n)

    if n == 1:
        return 1
    else:
        if n % 2 == 0:
           return hailstone(int(n / 2)) + 1
        else:
            return hailstone(int(n * 3 + 1)) + 1

# 1.5 Tutorial: (Optional)
# Define a function make fn repeater which takes in a one-argument function
# f and an integer x. It should return another function which takes in one
# argument, another integer. This function returns the result of applying f to
# x this number of times.
# Make sure to use recursion in your solution.

def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """

    # f2(2) = 
            #f(f2(1): f(2) = 3
            # f(f2(0)): f(1) = 2
            #     f2(0)
            #         1
    def f2(n):
        if n == 0:
            return x
        else:
            return f(f2(n - 1)) 
    return f2

# 1.6
# Implement the recursive is prime function. Do not use a while loop, use
# recursion. As a reminder, an integer is considered prime if it has exactly two
# unique factors: 1 and itself.
def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """

    if n == 1:
        return False

    def prime_helper(n, k):
        value = 0
        # done searching, no divisor other than 1 and itself. return true value
        if k >= n:
            value = 1
            return 1
        # check divisors expect 1 and n, if found return false value denotes not prime
        elif n % k == 0:
            value = 0
            return value
        else:
            return prime_helper(n, k + 1) + value
    # convert either true value or false value to boolean value
    return bool(prime_helper(n, 2))

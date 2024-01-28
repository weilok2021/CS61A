HW_SOURCE_FILE=__file__


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x == 8:
        return 1
    elif x < 10:
        return 0
    else:
        # check number of digit 8 in each recursive call
        return (1 if x % 10 == 8 else 0) + num_eights(x // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"

    def helper(count, value, one):
        if count > n:
            return value
        else:
            #value += one
            if num_eights(count) or (count % 8 == 0):
                # one *= -1
                return helper(count + 1, value + one, one * -1)
            else:
                return helper(count + 1, value + one, one)
            #return helper(count + 1, value, one)

    return helper(1, 0, 1)
    
    # iterative solution
    # count = 1 # to keep track the ping pong index
    # value = 0
    # one = 1
    # while count <= n:
    #     value += one
    #     if num_eights(count) or (count % 8 == 0):
    #         # flip the sign of one, to swap between increasing order or decreasing order, i+1 or i-1
    #         one *= -1 
    #     count += 1

    # return value

def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"

    # the problem is I need to compare each integers in between with the list from first_digit + 1 to last_digit - 1

    # base case
    # when the list has been checked from last_digit - 1 to first_digit
    # integer in between


    # t = n // 10 # trim it first, don't have to check the last digit
    # if n > 10:
    #     not_found = last_digit(n) - first_digit(n) - 1 
    # else:
    #     not_found = 0

    # # previous digit: to keep track duplicate integers in between 
    # prev = 0
    # while t > 0:
    #     digit = t % 10
    #     i = last_digit(n) - 1 
    #     # range of numbers to compare
    #     while i > first_digit(n):
    #         # print(i)
    #         # there's missing number in between
    #         # digit != prev is to check duplicates
    #         if digit == i and digit != (prev):
    #             not_found -= 1
    #         i -= 1
    #     prev = digit
    #     t = t // 10
    # return not_found

    # Pre-compute the total numbers between last integer and first integer
    if n > 10:
        missing = last_digit(n) - first_digit(n) - 1 
    else:
        missing = 0

    # to keep track previous integer, which I don't have to increment exist if I already found in previous search
    prev = 0
    trimmed_n = n // 10

    def search_existed(n, trimmed_n, digit, i, missing, prev):
        """ return the number of existing numbers between first_digit, and last_digit

        >>>search_existed(123456, 12345, 5, 5, 4, 0)
        4 # There are no missing numbers, 2,3,4,5 are existed between 1 and 6

        >>>search_existed(19, 1, 0, 8, 7, 0)
        0 # There are 7 missing numbers in between: 2,3,4,5,6,7,8. And none of this existed.
        
        """

        def search(i, digit, first_digit, prev):
            count = 0
            # search finish
            if i <= first_digit:
                return count
            else:
                # find existed integer in between, which means integer that's not missing
                if digit == i and digit != (prev):
                    count = 1
                    return 1
                # otherwise, continue searching
                return search(i - 1, digit, first_digit, prev) + count
         
        existed = search(i, digit, first_digit(n), prev)
        prev = digit

        if trimmed_n == 0:
            return existed
        else:
            return search_existed(n, trimmed_n // 10, trimmed_n % 10, last_digit(n) - 1, missing, prev) + existed

    return missing - search_existed(n, trimmed_n, trimmed_n % 10, last_digit(n) - 1, missing, prev)

def first_digit(n):
    if n < 10:
        return n
    else:
        return first_digit(n // 10)

    # while n > 9:
    #     n = n // 10
    # return n

def last_digit(n):
    return n % 10

def next_largest_coin(coin):
    """Return the next coin. 
    >>> next_largest_coin(1)
    5
    >>> next_largest_coin(5)
    10
    >>> next_largest_coin(10)
    25
    >>> next_largest_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Return the number of ways to make change for total using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])                                          
    True
    """
    "*** YOUR CODE HERE ***"


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'


# Function examples

# Implementing functions

def remove(n, digit):
    """
    DIGIT is the digit we need to remove from any non negative N integers
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313

    """

    keep = 0
    places = 1 # start counting from oneth places, to tenth, hundredth etc..
    while n > 0:
        n, last = n // 10, n % 10
        if last == digit:
            places /= 10
        elif last != digit:
            keep += (last * places)
        # move to next places
        places *= 10 
    return int(keep)

def reverse(x):
    is_negative = False

    if x < 0:
        is_negative = True
        x = -1 * x

    exp = len(str(x)) - 1
    keep = 0

    while x > 0:
        x, last = x // 10, x % 10
        keep += last * pow(10, exp)
        exp -= 1
    
    if is_negative:
        keep *= -1
    
    # x = keep
    if not (pow(-2, 31) <= keep <= pow(2,31) - 1):
        return 0

    return keep

def pow(x, n):
    if not(-100.0 < x < 100.0 and (-2 ** 31) < n < (2 ** 31) - 1 and isinstance(n, int) and
    (x != 0 or n > 0) and (-10 ** 4) <= (x ** n) <= (10 ** 4)):
        return 0
    if n == 0:
        return 1
    if n < 0:
        n = abs(n)
        x = 1 / x
    return x * pow(x, n - 1) 

# def neg_pow(x, n):
#     if n 
# print numbers by recursion example

def cascade(n):
    """
    >>>cascade(123)
    123
    12
    1
    12
    123

    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)
    
def inverse_cascade(n):
    """

    >>>inverse_cascade(123)
    1
    12
    123
    12
    1

    """
    f_then_g(f, g ,n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n // 10)

grow = lambda n: f_then_g()
shrink = lambda n: f_then_g()
def f(n):
    if n < 10:
        print(n)
    else:
        f(n // 10)
        print(n)

def g(n):
    print(n)
    if n < 10:
        return None
    g(n // 10)

    


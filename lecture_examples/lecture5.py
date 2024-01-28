# sum numbers in list recursively
def sum_list(L):
    """

    >>>sum_list([2, 4, 1, 5])
    12

    """
    if L == []:
        return 0
    else:
        # recursively add the first number of list and the remaining list.
        return L[0] + sum_list(L[1:]) 

# reverse a string recursively
def reverse(s):
    """
    s2 += [s[end_i] for s[end_i] in s]

    >>>reverse("draw")
    'ward'

    >>>reverse('a')
    'a'

    >>>reverse('aa')
    'aa'

    >>>reverse('aba')
    'aba'

    """

    if len(s) == 1:
        return s
    else:
        return reverse(s[1: ]) + s[0]
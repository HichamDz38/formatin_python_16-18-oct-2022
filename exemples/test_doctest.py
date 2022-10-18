def fact(n):
    """
        paramètre n : (int) un entier
        valeur renvoyée : (int) la factorielle de n.

    CU : n >= 0

    Exemples :

    >>> fact(3)
    6
    >>> fact(5)
    120
    """
    res = 1
    for i in range(2, n + 1):
       res = res * i
    return res
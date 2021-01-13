def func(a, b):
    """
    >>> func(5, 2)
    25
    >>> func(10, 2)
    100
    """
    return a ** b

if __name__ == "__main__":
    import doctest
    doctest.testmod()


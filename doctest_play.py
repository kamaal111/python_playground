def self_test_funcion(n: int) -> int:
    """Returns just the same number

    >>> self_test_funcion(22)
    22

    Dude, why are you giving this function a string while it obviously wants a integer
    >>> self_test_funcion("K")
    Traceback (most recent call last):
    ...
    TypeError: can't multiply sequence by non-int of type 'str'
    """
    return int(n * n / n)

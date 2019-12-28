def is_braces_sequence_correct(seq: str) -> bool:
    """
    :param seq: str
    :return: bool

    Check correctness of braces sequence in statement
    >>> is_braces_sequence_correct("()(())")
    True
    >>> is_braces_sequence_correct("(){}[{}]")
    True
    >>> is_braces_sequence_correct("(")
    False
    >>> is_braces_sequence_correct("))({")
    False
    >>> is_braces_sequence_correct("}]]()")
    False
    """

    previous=''
    while seq != previous: previous, seq = seq, seq.replace('[]', '').replace('{}', '').replace('()', '')
    return not seq


if __name__ == '__main__':
    import doctest

    # doctest.testmod()
is_braces_sequence_correct("(){}[{}]")

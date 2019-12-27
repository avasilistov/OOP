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
    correspondent = dict(zip("([{", ")]}"))
    stack = []
    for brace in seq:
        if brace in "({[":
            stack.append(brace)
            continue
        elif brace in ")}]":
            if stack == []:
                return False
            left = stack.pop()
            if correspondent[left] != brace:
                return False

    return stack == []


if __name__ == '__main__':
    import doctest

    doctest.testmod()

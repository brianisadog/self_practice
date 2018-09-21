def valid_parentheses(d, parentheses):
    """
    :type d: dict[str: str]
    :type parentheses: str
    :rtype: bool
    """
    stack = []

    for char in parentheses:
        if char in d:
            stack.append(d[char])
        else:
            if len(stack) == 0 or char != stack.pop():
                return False

    return len(stack) == 0


d = {'[': ']', '{': '}', '(': ')'}

parentheses = ''  # True
print(valid_parentheses(d, parentheses))

parentheses = '[({})]'  # True
print(valid_parentheses(d, parentheses))

parentheses = '[({})][]([]){}'  # True
print(valid_parentheses(d, parentheses))

parentheses = '[[[][]]'  # False
print(valid_parentheses(d, parentheses))

parentheses = '[[[]]}'  # False
print(valid_parentheses(d, parentheses))

parentheses = '[({'  # False
print(valid_parentheses(d, parentheses))

parentheses = '}{'  # False
print(valid_parentheses(d, parentheses))

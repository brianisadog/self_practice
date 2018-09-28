def reverse(x):
    """
    :type x: int
    :rtype: int

    Assume we are dealing with an environment which could only store integers
    within the 32-bit signed integer range: [−2^31,  2^31 − 1].
    For the purpose of this problem, assume that your function returns 0 when
    the reversed integer overflows.
    """
    y = str(x)
    if '-' == y[0]:
        z = int('-' + y[:0:-1])
    else:
        z = int(y[::-1])
    return z if -(2 ** 31) <= z <= (2 ** 31 - 1) else 0


print(reverse(0))  # 0
print(reverse(-(2 ** 31)))  # 0
print(reverse((2 ** 31 - 1)))  # 0
print(reverse((2 ** 16 - 1)))  # 65535 -> 53556
print(reverse(-343465674))  # -476564343
print(reverse(49))  # 94

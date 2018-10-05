def missing_number(nums):
    """
    :type nums: List[int]
    :rtype: int

    Given an array containing n distinct numbers taken from
    0, 1, 2, ..., n, find the one that is missing from the array.
    """
    sum1 = sum(nums)
    sum2 = len(nums) * (len(nums) + 1) / 2
    return int(sum2 - sum1)


test_l = [3, 0, 1]
print(missing_number(test_l))

test_l = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missing_number(test_l))

test_l = []
print(missing_number(test_l))

def license_key_formatting(s, k):
    """
    :param s: string to be formatted
    :type s: str
    :param k: count of characters between '-'
    :type k: int
    :rtype: str

    Given a number k, we would want to reformat the strings such that
    each group contains exactly k characters, except for the first group
    which could be shorter than k, but still must contain at least one
    character. Furthermore, there must be a dash inserted between two
    groups and all lowercase letters should be converted to uppercase.

    Example:
    Input: s = '5F3Z-2e-9-w', k = 4
    Output: '5F3Z-2E9W'
    Explanation: The string s has been split into two parts, each part has 4 characters.
                 Note that the two extra dashes are not needed and can be removed.
    """

    def chunk(a, l):
        """
        yield creates a generator and does not store in memory after it has been used.
        We only goes through the string once, so no need to store in memory.
        This function breaks the string into chunks with length l, which is k.
        """
        for i in range(0, len(s), l):
            yield a[i:i + l]

    """
    Reverse the string since the leading chunk characters could be less than k.
    So we will create chunks backward. Convert alphabets to upper case and remove '-'.
    
    Use join to insert '-' between chunks then reverse the string again to make the order back to normal.
    """
    a = s[::-1].upper().replace('-', '')
    res = '-'.join(list(chunk(a, k)))[::-1]

    return res if not res.startswith('-') else res[1:]  # remove leading '-' if needed


test_s = '5F3Z-2e-9-w'
test_k = 4
print(license_key_formatting(test_s, test_k))

test_s = '2-5g-3-J'
test_k = 2
print(license_key_formatting(test_s, test_k))

test_s = ''
test_k = 1
print(license_key_formatting(test_s, test_k))

test_s = '2ajo34irucuamcr3r90pmraciurJ'
test_k = 6
print(license_key_formatting(test_s, test_k))

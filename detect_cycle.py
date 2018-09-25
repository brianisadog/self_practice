from util.ListNode import ListNode


def detect_cycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            print(f'slow = {slow.val}')
            print(f'fast = {fast.val}')
            slow = slow.next
            fast = fast.next.next
    except:
        return None

    # hit here means there is cycle
    while head is not slow:
        head = head.next
        slow = slow.next

    return head

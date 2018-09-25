from util.ListNode import ListNode


def detect_cycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    try:
        slow = head.next
        fast = head.next.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
    except:
        return None

    # hit here means there is cycle
    while head is not slow:
        head = head.next
        slow = slow.next

    return head


# None
node = ListNode(val=1)
print(detect_cycle(node))

# None
node2 = ListNode(val=2)
node.next = node2
print(detect_cycle(node))

# 1
node2.next = node
print(detect_cycle(node).val)

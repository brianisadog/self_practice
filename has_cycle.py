from util.ListNode import ListNode


def has_cycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    try:
        fast = head.next
        while head is not fast:
            head = head.next
            fast = fast.next.next
        return True
    except:
        return False


# False
node = ListNode(val=1)
print(has_cycle(node))

# False
node2 = ListNode(val=2)
node.next = node2
print(has_cycle(node))

# True
node2.next = node
print(has_cycle(node))

from util.TreeNode import TreeNode


def is_same_tree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool

    Given two binary trees, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
    """
    if p and q:
        return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    return p is q

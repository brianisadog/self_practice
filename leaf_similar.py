from util.TreeNode import TreeNode


def leaf_similar(root1, root2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: bool

    Consider all the leaves of a binary tree.
    From left to right order, the values of those leaves form a leaf value sequence.
    Two binary trees are considered leaf-similar if their leaf value sequence is the same.

    Example:
             3
           /  \
          5    1
        / \   / \
       6  2  9  8
         / \
        7  4
    Leafs = [6, 7, 4, 9, 8]
    """
    return dfs(root1) == dfs(root2)


def dfs(node):
    if not node:
        return []
    elif not node.left and not node.right:
        return [node.val]
    return dfs(node.left) + dfs(node.right)


# Build example tree
a1 = TreeNode(3)
a2 = TreeNode(5)
a3 = TreeNode(1)
a1.left = a2
a1.right = a3
a4 = TreeNode(6)
a5 = TreeNode(2)
a2.left = a4
a2.right = a5
a6 = TreeNode(9)
a7 = TreeNode(8)
a3.left = a6
a3.right = a7
a8 = TreeNode(7)
a9 = TreeNode(4)
a5.left = a8
a5.right = a9

b1 = TreeNode(10)
b2 = TreeNode(34)
b3 = TreeNode(-6)
b1.left = b2
b1.right = b3
b4 = TreeNode(6)
b5 = TreeNode(54)
b2.left = b4
b2.right = b5
b6 = TreeNode(9)
b7 = TreeNode(8)
b3.left = b6
b3.right = b7
b8 = TreeNode(7)
b9 = TreeNode(4)
b5.left = b8
b5.right = b9

c1 = TreeNode(42)
c2 = TreeNode(7)
c1.right = c2

print(leaf_similar(a1, b1))  # True
print(leaf_similar(a1, c1))  # False
print(leaf_similar(c1, c1))  # True
print(leaf_similar(b1, None))  # False
print(leaf_similar(None, None))  # True

"""
Given the root node of a binary search tree, return the sum of values of all nodes with a value in the range [low, high].



Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
"""


# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, node: TreeNode, low: int, high: int) -> int:

        # If no element in the binary tree
        if not node:
            return 0

        # If the value is root value is higher then we focus on the left node of the tree
        if node.val > high:
            return self.rangeSumBST(node.left, low, high)

        # In this we can see that if the value of the node is less than the low (We ignore the
        # Left tree of and shift to the right(right node) sub tree for arranged sub trees ( root > root.left,

        elif node.val < low:
            return self.rangeSumBST(node.right, low, high)

        # If the value is in range we add the value and perform BST to both trees
        else:
            return self.rangeSumBST(node.left, low, high) + node.val + self.rangeSumBST(node.right, low, high)


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)

print(Solution().rangeSumBST(root, 7, 15))

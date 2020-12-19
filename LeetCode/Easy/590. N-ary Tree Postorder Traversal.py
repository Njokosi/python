"""
Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).



Follow up:

Recursive solution is trivial, could you do it iteratively?
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []


class Solution:
    def postorder(self, root_node):
        def dfs(node, result):
            for child in node.children:
                if child:
                    dfs(child, result)
            result.append(node.val)

        post_order_tree = []
        if root_node:
            dfs(root_node, post_order_tree)
        return post_order_tree


root = Node(1)
root.children.append(Node(3))
root.children.append(Node(2))
root.children.append(Node(2))
root.children[0].children.append(Node(5))
root.children[0].children.append(Node(6))

print(Solution().postorder(root))
""""
https://leetcode.com/problems/n-ary-tree-preorder-traversal/

Given an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of childrenren is separated by the null value (See examples).



Follow up:

Recursive solution is trivial, could you do it iteratively?



Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]


Constraints:

The height of the n-ary tree is less than or equal to 1000
The total number of nodes is between [0, 10^4]
"""


# Definition for a Node.
class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = []


class Solution:
    def preorder(self, root_node: Node) -> list:
        def dfs(node, result):
            result.append(node.val)
            for child in node.children:
                if child:
                    dfs(child, result)

        pre_order_tree = []
        if root_node:
            dfs(root_node, pre_order_tree)
        return pre_order_tree


root = Node(1)
root.children.append(Node(2))
root.children.append(Node(3))
root.children.append(Node(5))
root.children[0].children.append(Node(5)) 
root.children[0].children[0].children.append(Node(9))
root.children[0].children.append(Node(7))
root.children[0].children[1].children.append(Node(0))
root.children[0].children[1].children.append(Node(12))
root.children[0].children[1].children.append(Node(13)) 
root.children[2].children.append(Node(6))
root.children[2].children.append(Node(8))
root.children[2].children.append(Node(9))


print(Solution().preorder(root))
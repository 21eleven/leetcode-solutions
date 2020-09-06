"""
1305. All Elements in Two Binary Search Trees
Medium

Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:

Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:

Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:

Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        output = []
        nodes = deque()
        if root1:
            nodes.append(root1)
        if root2:
            nodes.append(root2)
        while nodes:
            n = nodes.popleft()
            output.append(n.val)
            if l := n.left:
                nodes.append(l)
            if r := n.right:
                nodes.append(r)
        return sorted(output)

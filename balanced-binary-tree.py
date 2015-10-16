#!/usr/bin/env python
# encoding: utf-8

"""
https://leetcode.com/discuss/22898/the-bottom-up-o-n-solution-would-be-better
method is based on DFS. Instead of calling depth() explicitly for each child node, we return the height of the current node in DFS recursion. When the sub tree of the current node (inclusive) is balanced, the function dfsHeight() returns a non-negative value as the height. Otherwise -1 is returned. According to the leftHeight and rightHeight of the two children, the parent node could check if the sub tree is balanced, and decides its return value.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfsHeight(root) != -1
        
    def dfsHeight(self, node):
        if not node: return 0

        leftHeight = self.dfsHeight(node.left)
        if leftHeight == -1: return -1

        rightHeight = self.dfsHeight(node.right)
        if rightHeight == -1: return -1

        if abs(leftHeight - rightHeight) > 1: return -1

        return max(leftHeight, rightHeight) + 1

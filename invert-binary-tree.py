"""
https://leetcode.com/problems/invert-binary-tree/
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return root
        
        root.left, root.right = root.right, root.left
        
        if getattr(root.left, "left", None) or getattr(root.left, "right", None):
            self.invertTree(root.left)
        
        if getattr(root.right, "left", None) or getattr(root.right, 'right', None):
            self.invertTree(root.right)
            
        return root

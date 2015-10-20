# tion for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
            
        if left.val == right.val:
            outer = self.isMirror(left.left, right.right)
            inner = self.isMirror(left.right, right.left)
            return outer and inner
        else:
            return False

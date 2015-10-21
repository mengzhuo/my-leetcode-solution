# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.result = []
        self.buildOrder(root, 0)
        return self.result
    
    def buildOrder(self, root, depth):
        
        if not root:
            return None
        
        if len(self.result) == depth:
            self.result.append([])
            
        self.result[depth].append(root.val)
        self.buildOrder(root.left, depth+1)
        self.buildOrder(root.right, depth+1)

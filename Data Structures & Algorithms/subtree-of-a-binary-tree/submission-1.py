# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        def sametree(p: Optional[TreeNode],q: Optional[TreeNode])->bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            left = sametree(p.left, q.left)
            right = sametree(p.right, q.right)
            return left and right
        
        if sametree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
            
        


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(cur):
            if not cur:
                return
            
            cur.left,cur.right = cur.right,cur.left
            helper(cur.left)
            helper(cur.right)
        
        helper(root)
        return root
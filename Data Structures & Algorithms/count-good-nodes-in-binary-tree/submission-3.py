# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good = 0
        def helper(cur,val):
            nonlocal good
            if not cur:
                return
            
            if cur.val>=val:
                good += 1
                val = cur.val

            
            helper(cur.left,val)
            helper(cur.right,val)
        
        helper(root,-9999)
        return good
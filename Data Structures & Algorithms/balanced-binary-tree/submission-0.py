# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(cur,val):
            if val==-1:
                return -1
            if not cur:
                return val
            left = helper(cur.left,1+val)
            right = helper(cur.right,1+val)

            if abs(left-right)>1:
                return -1
            return max(left,right)
        
        final = helper(root,0)
        return final != -1
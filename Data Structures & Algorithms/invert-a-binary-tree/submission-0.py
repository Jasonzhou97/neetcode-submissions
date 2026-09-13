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
                return None
            cur.left, cur.right = helper(cur.right),helper(cur.left)
            return cur
        return helper(root)
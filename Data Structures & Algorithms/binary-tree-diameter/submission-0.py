# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        maxdiameter = 0

        def dfs(cur):
            if not cur:
                return -1
            nonlocal maxdiameter
            left = 1+dfs(cur.left)
            right = 1+dfs(cur.right)

            maxdiameter = max(maxdiameter,left+right)
            return max(left,right)
        dfs(root)
        
        return maxdiameter
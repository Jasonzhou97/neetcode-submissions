# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        total = 0
        maxsofar = root.val
        def helper(cur,maxsofar):
            if not cur:
                return 0
            nonlocal total
            if cur.val>=maxsofar:
                total+=1
                maxsofar = cur.val
            helper(cur.left,maxsofar)
            helper(cur.right,maxsofar)

        helper(root,maxsofar)
        return total
            
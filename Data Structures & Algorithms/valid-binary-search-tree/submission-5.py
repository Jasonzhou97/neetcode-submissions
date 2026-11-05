class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(cur,low,high):
            if not cur:
                return True
            if cur.val>= high or cur.val<=low:
                return False
            
            return helper(cur.left,low,cur.val) and helper(cur.right,cur.val,high)

        return helper(root, float("-inf"), float("inf"))
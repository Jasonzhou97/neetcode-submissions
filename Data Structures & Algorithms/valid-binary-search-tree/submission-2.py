class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(cur,smallest,largest):
            if not cur:
                return True
            if not (smallest < cur.val < largest):
                return False
            else:
                return helper(cur.left,smallest,cur.val) and helper(cur.right,cur.val,largest)
    
        return helper(root,float('-inf'),float('inf'))




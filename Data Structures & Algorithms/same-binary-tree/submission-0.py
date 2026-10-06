
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            if p.val != q.val:
                return False
            
            return helper(p.left,q.left) and helper(p.right,q.right)
        
        return helper(p,q)

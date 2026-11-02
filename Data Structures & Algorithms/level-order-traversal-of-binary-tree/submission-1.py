
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def bfs(cur):
            if not cur:
                return None
            queue = deque([cur])
            res = []
            while len(queue)!=0:
                level = []
                for i in range(len(queue)):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                res.append(level)
            return res


        return bfs(root)
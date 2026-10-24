class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        
        visited = set()
        def get_neighbours(r,c):
            delta_r = [-1,0,1,0]
            delta_c = [0,1,0,-1]
            res = []
            for i in range(len(delta_r)):
                nextr = delta_r[i] + r
                nextc = delta_c[i] + c
                if (0 <= nextr < len(board) and 0 <= nextc < len(board[0])
                        and board[nextr][nextc] == 'O'): 
                    res.append((nextr,nextc))
            return res

        def bfs(i,j):
            queue = deque([(i,j)])
            board[i][j] = 'T'
            visitedhere = set()
            while len(queue)!=0:
                r,c = queue.popleft()
                if (r,c) not in visitedhere:
                    visitedhere.add((r,c))
                    for nr, nc in get_neighbours(r, c):
                        board[nr][nc] = 'T'
                        queue.append((nr, nc))
            
        def check_edge(i,j):
            if i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1:
                return True
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and check_edge(i, j):
                    visited.add((i,j))
                    bfs(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
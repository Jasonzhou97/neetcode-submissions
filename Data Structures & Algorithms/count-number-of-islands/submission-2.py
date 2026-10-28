
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        


        def get_neighbours(r,c,grid):
            delta_r = [-1,0,1,0]
            delta_c = [0,1,0,-1]
            res = []
            for i in range(len(delta_r)):
                nextr = r+delta_r[i]
                nextc = c+delta_c[i]
                if 0<=nextr<len(grid) and 0<=nextc<len(grid[0]):
                    res.append((nextr,nextc))
            return res

        visited = set()
        islands = 0
        def bfs(r,c):
            queue = deque([(r,c)])
            while len(queue)!=0:
                r,c = queue.popleft()
                if grid[r][c] == '1'and (r,c) not in visited:
                    visited.add((r,c))
                    for nextr,nextc in get_neighbours(r,c,grid):
                        if (nextr,nextc) not in visited and grid[nextr][nextc] == '1':
                            queue.append((nextr,nextc))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]=='1':
                    bfs(i,j)
                    islands+=1

        return islands



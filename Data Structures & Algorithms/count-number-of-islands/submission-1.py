class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def get_neighbours(r,c,grd):
            delta_r = [-1,0,1,0]
            delta_c = [0,1,0,-1]
            res = []
            for i in range(len(delta_r)):
                nextr = r+delta_r[i]
                nextc = c+delta_c[i]

                if 0<=nextr<len(grd) and 0<=nextc<len(grd[0]):
                    res.append((nextr,nextc))
            
            return res
        
        visited = set()
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j]=="1":
                    # start bfs
                    queue = deque([(i,j)])
                    while len(queue)!=0:  
                        r,c = queue.popleft()
                        if (r,c) not in visited:  
                            if grid[r][c] == "1":
                                visited.add((r,c))
                                for row,col in get_neighbours(r,c,grid):
                                    if (row,col) not in visited:
                                        queue.append((row,col))

                    islands += 1

                    
        return islands

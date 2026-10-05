class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def get_neighbours(r,c,grid):
            delta_r = [-1,0,1,0]
            delta_c = [0,1,0,-1]
            res = []
            for i in range(len(delta_c)):
                nextr = r+delta_r[i]
                nextc = c+delta_c[i]
                if 0<=nextr<len(grid) and 0<=nextc<len(grid[0]):
                    res.append((nextr,nextc))
            return res
        
        visited = set()
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    queue = deque([(i,j)])
                    area = 0
                    while len(queue)!=0:
                        r,c = queue.popleft()
                        if grid[r][c] == 1 and (r,c) not in visited:
                            visited.add((r,c))
                            queue.extend(get_neighbours(r,c,grid))
                            area += 1
                    
                    maxArea = max(area,maxArea)
        return maxArea
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        healthy_oranges = 0
        queue = deque([])
        # find number of healthyoranges and starting addresses
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    healthy_oranges += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        minutes = 0
        # do a bfs
        def get_neighbours(r,c,grid):
            delta_r = [-1,0,1,0]
            delta_c = [0,1,0,-1]
            res = []
            for i in range(4):
                nextr = delta_r[i] + r
                nextc = delta_c[i] + c
                if 0<=nextr<len(grid) and 0<=nextc<len(grid[0]) and grid[nextr][nextc]==1:
                    grid[nextr][nextc] = 2
                    res.append((nextr,nextc))
            return res
        visited = set()
        if healthy_oranges==0:
            return 0
        while len(queue)!=0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if grid[r][c] == 1 and (r,c) not in visited:
                    visited.add((r,c))
                    healthy_oranges -= 1
                    grid[r][c] = 2
                    queue.extend(get_neighbours(r,c,grid))
                elif grid[r][c] == 2 and (r,c) not in visited:
                    visited.add((r,c))
                    rotten = get_neighbours(r,c,grid)
                    healthy_oranges -= len(rotten)
                    queue.extend(rotten)
            minutes += 1
            if healthy_oranges==0:
                return minutes
        return -1
                
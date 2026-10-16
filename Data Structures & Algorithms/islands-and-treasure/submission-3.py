
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        def get_neighbours(r,c,grid):
            delta_r = [-1,0,1,0]
            delta_c = [0,1,0,-1]
            res = []
            for i in range(4):
                nextr = r+delta_r[i]
                nextc = c+delta_c[i]
                if 0<=nextr<len(grid) and 0<=nextc<len(grid[0]):
                    res.append((nextr,nextc))
                
            return res
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
        distance = 0
        while len(queue) != 0:
            distance += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                for nextr, nextc in get_neighbours(r, c, grid):
                    if grid[nextr][nextc] == INF:
                        grid[nextr][nextc] = distance
                        queue.append((nextr, nextc))
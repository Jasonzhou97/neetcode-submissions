class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minHeap = []
        for i in range(len(points)):
            x,y = points[i][0],points[i][1]
            distance = math.sqrt(x**2+y**2)
            minHeap.append((distance,x,y))
        
        heapq.heapify(minHeap)
        res = []
        for n in range(k):
            dis,x,y = heapq.heappop(minHeap)
            res.append([x,y])
        return res
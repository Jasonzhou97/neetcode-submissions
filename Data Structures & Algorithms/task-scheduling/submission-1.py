class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxheap = [-n for n in count.values()]
        heapq.heapify(maxheap)

        time = 0
        q = deque()
        while maxheap or q:
            time += 1
            if not maxheap:
                # jump to earlist task ready time
                time = q[0][1]
            else:

                task = heapq.heappop(maxheap)
                cnt = 1+task
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1] == time:
                t = q.popleft()
                heapq.heappush(maxheap,t[0])
        
        return time
                
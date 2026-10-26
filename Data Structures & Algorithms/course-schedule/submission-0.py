class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree = [0]*numCourses

        adj = [[] for i in range(numCourses)]

        for src,dest in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        finish = 0
        while len(q)!=0:
            node = q.popleft()
            finish+=1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        
        return finish == numCourses
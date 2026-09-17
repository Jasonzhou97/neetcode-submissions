import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        qu = Counter(nums)
        qu = list(qu.items())
        qu.sort(key = lambda x: (x[1],x[0]),reverse=True)

        res = []
        for i in range(k):
            res.append(qu[i][0])
        return res
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ls = [0]*len(cost)

        ls[0] = cost[0]
        ls[1] = cost[1]

        for i in range(2,len(cost)):
            ls[i] = min(ls[i-2],ls[i-1])+cost[i]
        return min(ls[-1],ls[-2])
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        for num in nums:
            res += [ls + [num] for ls in res]
        
        return res
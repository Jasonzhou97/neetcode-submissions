class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        for n in nums:
            new_res = []
            for subset in res:
                subset_copy = subset.copy()
                subset_copy.append(n)
                new_res.append(subset_copy)
            res.extend(new_res)
        return res

            

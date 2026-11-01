class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for i in range(len(nums)):
            for subset in res[:]:
                newcomb = subset+[nums[i]]
                res.append(newcomb)
        return res


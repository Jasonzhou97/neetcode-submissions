class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -99999
        pref,suff = 0,0

        for i in range(len(nums)):
            pref = nums[i] * (pref if pref else 1)
            suff = nums[len(nums)-i-1] * (suff if suff else 1)
            res = max(res,max(pref,suff))
        
        return res
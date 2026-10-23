class Solution:
    def rob(self, nums: List[int]) -> int:
        ls = [0]*len(nums)

        if len(nums)<2:
            return max(nums)
        ls[0] = nums[0]
        ls[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            ls[i] = max(ls[i-2]+nums[i],ls[i-1])
        return max(ls[-1],ls[-2])
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        res = nums[0]

        while r>=l:
            if nums[r]>nums[l]:
                res = min(res,nums[l])
                break
            
            middle = (l+r)//2
            mid = nums[middle]
            res = min(res,mid)
            if mid>=nums[l]:
                l = middle + 1
            else:
                r = middle - 1
        
        return res
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0,len(nums)-1

        while r>=l:
            mid = (l+r)//2
            num = nums[mid]
            if num==target:
                return mid
            if num>target:
                r=mid-1
            else:
                l=mid+1
        return -1
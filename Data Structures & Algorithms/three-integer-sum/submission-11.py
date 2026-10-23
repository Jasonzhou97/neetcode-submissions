class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()
        for i in range(len(nums)):
            l ,r = i+1, len(nums)-1
            cur = nums[i]
            while r>l:
                left = nums[l]
                right = nums[r]
                total = cur+left+right
                if total==0:
                    if [cur,left,right] not in res:
                        res.append([cur,left,right])
                    l+=1
                    r-=1
                elif total>0:
                    r-=1
                else:
                    l+=1
        
        return res
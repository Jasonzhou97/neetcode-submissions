class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            cur = nums[i]
            left = i+1
            right = len(nums)-1
            while right>left:
                r = nums[right]
                l = nums[left]
                if l+r+cur==0:
                    if [cur,l,r] not in res:
                        res.append([cur,l,r])
                    left += 1
                    right -= 1
                    continue
                elif l+r+cur>0:
                    right-=1
                elif l+r+cur<0:
                    left +=1
        return res
                    
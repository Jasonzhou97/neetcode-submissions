class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        TARGET = 0
        ls = []
        for i in range(len(nums)):
            left,right = i+1,len(nums)-1
            while right>left:
                total = nums[i]+nums[left]+nums[right]
                if total==TARGET:
                    if [nums[i],nums[left],nums[right]] not in ls:
                        ls.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                elif total>TARGET:
                    right-=1
                else:
                    left+=1
        
        return ls
        

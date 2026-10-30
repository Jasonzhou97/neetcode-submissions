class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i in range(len(nums)):
            dif = target - nums[i] 
            if nums[i] in diff.keys():
                return [diff[nums[i]],i]
            diff[dif] = i
        return -1
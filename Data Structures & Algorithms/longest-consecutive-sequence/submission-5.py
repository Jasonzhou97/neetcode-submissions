class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        if len(nums)<2:
            return len(nums)
        maxlength = 1
        for n in numset:
            # start of new seq
            if n-1 not in numset:
                length = 1
                while (n+length in numset):
                    length += 1
                    maxlength = max(maxlength,length)

        
        return maxlength
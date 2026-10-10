class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxseq = 0
        for n in numset:
            if n-1 not in numset:
                num = n
                leng = 0
                while num in numset:
                    num = num+1
                    leng += 1
                    maxseq = max(maxseq,leng)
        
        return maxseq
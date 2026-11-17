class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]

        for n in nums:
            new_perms = []
            for ls in res:
                for i in range(len(ls)+1):
                    pcopy = ls.copy()
                    pcopy.insert(i,n)
                    new_perms.append(pcopy)
                
                res = new_perms
        return res
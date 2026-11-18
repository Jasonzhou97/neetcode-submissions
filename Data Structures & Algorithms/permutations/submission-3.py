class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]

        for n in nums:
            new_perm = []
            for perm in res:
                for i in range(len(perm)+1):
                    pcopy = perm.copy()
                    pcopy.insert(i,n)
                    new_perm.append(pcopy)
            
            res = new_perm
        
        return res
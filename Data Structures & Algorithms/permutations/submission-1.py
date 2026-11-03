class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            new_perms = []
            for array in res:
                for i in range(len(array)+1):
                    p_copy = array.copy()
                    p_copy.insert(i,n)
                    new_perms.append(p_copy)
            res = new_perms
        
        return res

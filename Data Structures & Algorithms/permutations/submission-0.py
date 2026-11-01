class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            new_res = []
            for perm in res:
                # insert new number into every new possible position
                for i in range(len(perm)+1):
                    p_copy = perm.copy()
                    p_copy.insert(i,n)
                    new_res.append(p_copy)
            res = new_res
        
        return res
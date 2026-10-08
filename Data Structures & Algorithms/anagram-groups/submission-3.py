class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()

        for s in strs:
            # create a list to kepp track of freq as dict ant be keys
            ls = [0]*26
            for c in s:
                ls[ord(c)-ord('a')] += 1
            ls = tuple(ls)
            if ls in res.keys():
                res[ls].append(s)
            else:
                res[ls] = [s]
            
           
        
        return list(res.values())
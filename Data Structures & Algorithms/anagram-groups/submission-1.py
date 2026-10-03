class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}
        for s in strs:
            lst = [0]*26
            for c in s:
                lst[ord(c)-ord('a')] += 1
            if tuple(lst) not in dic:
                dic[tuple(lst)] = [(s)]
            else:
                dic[tuple(lst)].append(s)
        
        return list(dic.values())

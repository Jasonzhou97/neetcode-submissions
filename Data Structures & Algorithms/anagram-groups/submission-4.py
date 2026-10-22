class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}

        for c in strs:
            freq = [0]*26
            for char in c:
                freq[ord(char)-ord('a')] += 1
            freq = tuple(freq)
            if freq in dic:
                dic[freq].append(c)
            else:
                dic[freq] = [c]

        res = []
        for ls in dic.values():
            res.append(ls)
        return res
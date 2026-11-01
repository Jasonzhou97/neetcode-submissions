class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []

        freq = {}

        for string in strs:
            chars = [0]*26
            for c in string:
                chars[ord(c)-ord('a')] += 1
            chars = tuple(chars)
            if chars in freq:
                freq[chars].append(string)
            else:
                freq[chars] = [string]
        
        return [v for v in freq.values()]
                
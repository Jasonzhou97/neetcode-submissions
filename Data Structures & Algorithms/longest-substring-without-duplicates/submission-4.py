class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l ,r = 0,0
        lst = list(s)
        maxlen = 0
        seen = set()
        while r<len(s):
            while lst[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxlen = max(maxlen,r-l+1)
            r+=1
        
        return maxlen
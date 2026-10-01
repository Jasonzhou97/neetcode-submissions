class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,1
        if len(s)==0:
            return 0
        maxlength = 1
        length = 1
        window = set()
        window.add(s[l])
        while r<len(s) and l<r:
            while s[r] in window and r>l:
                window.remove(s[l])
                l+=1
                length-=1
            window.add(s[r])
            r+=1
            length+=1
            maxlength = max(length,maxlength)

        
        return maxlength
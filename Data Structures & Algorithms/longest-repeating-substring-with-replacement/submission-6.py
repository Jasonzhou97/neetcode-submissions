class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        charSet = set(s)
        

        for c in charSet:
            diff = 0
            l,r = 0,0
            while r<len(s):
                if s[r]!=c:
                    diff += 1
                while diff>k:
                    if s[l]!=c:
                        diff-=1
                    l+=1
                maxLen = max(maxLen,r-l+1)
                r+=1
        return maxLen

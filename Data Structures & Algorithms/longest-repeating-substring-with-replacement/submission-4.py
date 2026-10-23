class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r=0,0
        charSet = set(s)
        longest = 0

        for c in charSet:
            count = 0
            l = 0
            r = 0
            while r<len(s):
                if s[r]!=c:
                    count += 1
                while count>k:
                    if s[l] != c:
                        count-=1
                    l+=1
                longest = max(longest,r-l+1)
                r+=1
        return longest
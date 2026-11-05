class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charset = set(s)
        maxlen = 0
        for c in charset:
            l = 0
            count = 0
            for r in range(0,len(s)):
                if s[r]!=c:
                    count += 1
                while count > k:
                    if s[l]!=c:
                        count-=1
                    l+=1
                
                maxlen = max(maxlen,r-l+1)

        return maxlen
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charset = set(s)
        maxlength = 0
        for c in charset:
            l,r = 0,0
            count = 0
            while r<len(s):
                if s[r]!=c:
                    count+=1
                while count>k:
                    if s[l]!=c:
                        count-=1
                    l+=1
                
                maxlength = max(r-l+1,maxlength)
                r+=1
        return maxlength
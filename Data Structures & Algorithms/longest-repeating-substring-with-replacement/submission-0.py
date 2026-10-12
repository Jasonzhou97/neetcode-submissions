class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charset = set(s)
        maxlen = 0
        for c in charset:
            count = l = 0
            for i in range(len(s)):
                if s[i]==c:
                    count += 1
                
                while (i-l+1) - count > k:
                    if s[l]==c:
                        count-=1
                    l+=1
                
                maxlen = max(maxlen,i-l+1)
        
        return maxlen
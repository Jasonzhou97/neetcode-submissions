class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        resindex,reslen = 0,0

        for i in range(len(s)):

            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    resindex=l
                    reslen = r-l+1
                r = r+1
                l = l-1
            #even case, 2 alphabets as center
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>reslen:
                    resindex = l
                    reslen = max(reslen,r-l+1)
                r = r+1
                l = l-1
            
        return s[resindex:resindex+reslen]
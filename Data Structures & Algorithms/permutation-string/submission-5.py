class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        dic1 = [0]*26
        dic2 = [0]*26
        if len(s1)>len(s2):
            return False
        for c in s1:
            dic1[ord(c)-ord('a')] += 1
        
        l,r = 0,len(s1)-1
        for i in range(l,r+1):
            dic2[ord(s2[i])-ord('a')]+=1

        while r<len(s2):
            if dic2==dic1:
                return True
            
            left = s2[l]
            dic2[ord(left)-ord('a')]-=1
            l+=1
            r += 1
            if r==len(s2):
                return False
            right = s2[r]
            dic2[ord(right)-ord('a')]+=1

        return False

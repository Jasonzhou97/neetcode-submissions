class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # create freq table
        table1 = [0]*26
        table2 = [0]*26
        if len(s1)>len(s2):
            return False
        for c in s1:
            table1[ord(c)-ord('a')] += 1
        
        l = 0
        r = len(s1)-1
        for i in range(l,r+1):
            table2[ord(s2[i])-ord('a')] += 1
        while r<len(s2):
            if table1==table2:
                return True
            table2[ord(s2[l])-ord('a')]-=1
            l+=1
            r+=1

            if r>=len(s2):
                break
            table2[ord(s2[r])-ord('a')]+=1
        
        return False
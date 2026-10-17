class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        lst1 = [0]*26

        lst2 = [0]*26

        for c in s1:
            lst1[ord(c)-ord('a')] += 1
        i,r=0,0
        while r< len(s2):
            if r<len(s1):
                lst2[ord(s2[r])-ord('a')] += 1
                r+=1
                continue
            if lst1==lst2:
                return True
            lst2[ord(s2[i])-ord('a')] -= 1
            i += 1
            lst2[ord(s2[r])-ord('a')] += 1
            r += 1

        return lst1==lst2
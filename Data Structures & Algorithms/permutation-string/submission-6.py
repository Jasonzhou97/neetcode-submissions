class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map1 = [0]*26
        map2 = [0]*26

        if len(s2)<len(s1):
            return False
        for c in s1:
            map1[ord(c)-ord('a')] += 1
        
        l = 0
        r = 0
        for r in range(len(s2)):

            right = s2[r]
            map2[ord(right)-ord('a')] += 1

            if r-l+1>len(s1):
                map2[ord(s2[l])-ord('a')] -= 1
                l+=1
            if r-l+1==len(s1):
                if map1==map2:
                    return True
        return False
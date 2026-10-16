class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        lst1 = [0]*26
        lst2 = [0]*26
        for c in s1:
            lst1[ord(c)-ord('a')] += 1
        left,right = 0,0
        while right<len(s2):
            if lst1 == lst2:
                return True
            cur = s2[right]
            lst2[ord(cur)-ord('a')] += 1
            right+=1
            if right>=len(s1):
                if lst1 == lst2:
                    return True
                else:
                    lst2[ord(s2[left])-ord('a')]-=1
                    left+=1

        
        return False
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left,right = 0,len(s)-1
        s = s.lower()
        def isAlphanumeric(c):
            return c.isalnum()
        while right>=left:
            l,r = s[left],s[right]
            if not isAlphanumeric(l):
                left += 1
                continue
            if not isAlphanumeric(r):
                right -= 1
                continue
            if l!=r:
                return False

            left += 1
            right -= 1
        
        return True


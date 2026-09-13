class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        dic = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        i = 0
        while i<len(s):
            if s[i] in dic.values():
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                closing = dic[s[i]]
                if closing != stack.pop(-1):
                    return False
            i+=1
        return len(stack)==0
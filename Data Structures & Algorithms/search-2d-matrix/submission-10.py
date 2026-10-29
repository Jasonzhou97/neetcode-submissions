
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix),len(matrix[0])
        m,n = 0,(r*c)-1
        
        while n>=m:
            middle = (m+n)//2
            num = matrix[middle//c][middle%c]
            if num==target:
                return True
            elif num<target:
                m = middle+1
            else:
                n = middle-1
        
        return False
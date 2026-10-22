class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix),len(matrix[0])
        m,n = 0, (r*c)-1
        while n>=m:
            mid = (m+n)//2
            newr,newc = mid//c,mid%c
            num = matrix[newr][newc]
            if num==target:
                return True
            elif num<target:
                m = mid+1
            else:
                n = mid-1
        
        return False
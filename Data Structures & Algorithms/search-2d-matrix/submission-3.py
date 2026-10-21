class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row,col = len(matrix),len(matrix[0])
        l,r = 0, (row*col)-1
        while r>=l:

            mid = (l+r)//2
            num = matrix[mid//col][mid%col]
            if num==target:
                return True
            elif num>target:
                r = mid-1
            else:
                l = mid + 1
            
        return False

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0,len(heights)-1

        maxarea = 0

        while right>left:
            height = min(heights[left],heights[right])
            width = right-left
            area = height*width
            maxarea = max(area,maxarea)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
    
        return maxarea
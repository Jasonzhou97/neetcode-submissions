class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        left,right = 0,1

        while right < len(prices):
           if prices[left] > prices[right]:
                left = right
           else:
                diff = prices[right] - prices[left]
                maxPro = max(maxPro,diff)
           right+=1
        
        return maxPro
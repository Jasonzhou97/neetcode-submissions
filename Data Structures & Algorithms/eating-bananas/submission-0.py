class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # set min, max eating speed
        l,r = 1,max(piles)

        res = r

        while r>=l:
            
            #find mid point
            k = (l+r)//2
            total_time = 0
            for p in piles:
                total_time += math.ceil(float(p)/k)
            if total_time <= h:
                res = k
                r = k-1
            else:
                l = k+1
        
        return res


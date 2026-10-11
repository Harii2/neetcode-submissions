import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1 , max(piles)

        ans = -1 
        while l <= r:
            mid = (l + r) // 2 
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            
            if hours == h:
                ans = mid
                r = mid - 1
            elif hours < h:
                ans = mid 
                r = mid - 1
            else:
                l = mid + 1
        return ans 

        
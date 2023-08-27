class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l = 1
        res = r = piles[-1]
        
        
        while l <= r:
            total = 0
            k = (l + r) // 2
            for pile in piles:
                total += math.ceil(pile/k)
            if total > h:
                l = k + 1
            else:
                res = min(res, k)
                r = k - 1
        return res
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles:
            return 0

        left, right = 1, max(piles)
        while left < right:
            total_hours = 0
            mid = left + (right - left) // 2
            for pile in piles:
                total_hours += math.ceil(pile / mid)
            if total_hours <= h:
                right = mid
            else:
                left = mid + 1
        return left

        
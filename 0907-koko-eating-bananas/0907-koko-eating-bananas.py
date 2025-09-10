class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # check the edge case
        if not piles:
            return 0
        
        # initialize the left and right boundaries
        # left = 1, the minimum possible eating speed
        # right = max (piles), the maximum needed speed, can eat largest pile in one houre
        left, right = 1, max(piles)
        while left < right:

            total_hours = 0
            mid = left + (right - left) // 2

            # calculate the total hour for the current mid speed
            for pile in piles:
                total_hours += math.ceil(pile / mid)

            # if the total hours is smaller than the h, means it can eat slower, move the right pointer to mid
            if total_hours <= h:
                right = mid
            else:
            # otherwise, move the left pointer to the middle, 
                left = mid + 1
        return left

        
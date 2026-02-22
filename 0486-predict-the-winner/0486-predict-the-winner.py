from functools import lru_cache
from typing import List
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        @lru_cache(None)
        def f(i : int, j: int) ->int:
            # base case
            if i == j:
                return nums[i]

            #Minmax recurrence
            pick_left = nums[i] - f(i+1, j)
            pick_right = nums[j] - f(i,j-1)
            return max(pick_left, pick_right)
        return f(0, n-1) >= 0
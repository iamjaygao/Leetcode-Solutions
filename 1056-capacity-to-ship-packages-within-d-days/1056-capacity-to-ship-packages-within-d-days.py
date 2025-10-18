class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        1: Given a list of weights, and days used to ship the weights
        2: return the minimum capacity which can ship the weights in days
        """
        n = len(weights)
        if n  == days:
            return max(weights)
        min_weight = max(weights)
        max_weight = sum(weights)
        while min_weight <= max_weight:
            mid = (max_weight + min_weight) // 2
            if self.can_ship(weights, days, mid):
                max_weight = mid -1
            else:
                min_weight = mid +1
        return min_weight

    def can_ship(self, weights: List[int], days: int, mid:int):
        count = 1
        curr_weight = 0
        for weight in weights:
            if curr_weight + weight > mid:
                count += 1
                curr_weight = weight
                if count > days:
                    return False
            else:
                curr_weight += weight
        return True
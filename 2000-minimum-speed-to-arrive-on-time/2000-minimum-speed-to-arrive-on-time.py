class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        """
        1, Given the list of 'dist' representing the distnace of it ride
        2, Gien the hour, you can use to reach your des
        3, each train do interger hour, 
        4, return the minimum speed 
        """
        n = len(dist)
        left, right = 1, 10** 7
        res = -1
        while left <= right:
            total = 0
            mid = (right + left) // 2
            for i in range(n-1):
                total += math.ceil(dist[i]/ mid)
            total += dist[-1] / mid
            if total <= hour:
                res = mid 
                right = mid -1
            else:
                left = mid + 1
        return res
            
                

        

        
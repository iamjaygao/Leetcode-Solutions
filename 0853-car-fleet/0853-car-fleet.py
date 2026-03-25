class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse = True)

        fleets = 0
        pre_time = float("-inf")

        for p, s in pairs:
            curr_time = (target - p) / s
            if curr_time > pre_time:
                fleets += 1
                pre_time = curr_time 
        return fleets 
        
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        n = len(points)
        sorted_p = sorted(points)
        shoots = 1
        current_end = sorted_p[0][1]

        for i in range(1, n):
            if sorted_p[i][0] > current_end:
                shoots += 1
                current_end = sorted_p[i][1]
            else:
                current_end = min(current_end, sorted_p[i][1])

        return shoots
        
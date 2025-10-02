class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda x : x[1])
        arrow = 1
        current_pos = points[0][1]

        for i in range(len(points)):
            start, end = points[i]
            if start > current_pos:
                arrow += 1
                current_pos = end
        return arrow

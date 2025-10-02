class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # sort balloons by their end coordinate
        points.sort(key = lambda x : x[1])
        
        arrow = 1
        arrow_pos = points[0][1]    #shoot the arraw at the end of first ballon
        for i in range(1, len(points)):
            start, end = points[i]

            # if current balloon start after current arrow positions, need new arrow
            if start > arrow_pos:
                arrow += 1
                arrow_pos = end     #shoot new arrow at the end of current ballon
        return arrow

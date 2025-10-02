class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        count = 0
        intervals.sort(key = lambda x: x[1])
        current_pos = intervals[0][1]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start < current_pos:
                count += 1
            else:
                current_pos = end
        return count


        
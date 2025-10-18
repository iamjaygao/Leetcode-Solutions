class Solution:
    def can_place(self, position: List[int], m: int, d:int):
        count = 1
        prev = position[0]
        for p in position[1:]:
            if p - prev >= d:
                count += 1
                prev = p
                if count == m:
                    return True
        return False


    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        best = 0
        while left <= right:
            mid = (right + left) // 2
            if self.can_place(position,m, mid):
                best = mid 
                left = mid + 1
            else:
                right = mid - 1
        return best



    

    
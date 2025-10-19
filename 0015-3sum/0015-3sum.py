class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_array = sorted(nums)
        n = len(nums)
        result = []
        for i in range(n-2):
            if i > 0 and sorted_array [i] == sorted_array [i-1]:
                continue
            left = i + 1
            right = n-1
            target = -sorted_array [i]
            while left < right:
                sum_left_right = sorted_array [left] + sorted_array [right]
                if target == sum_left_right:
                    result.append([sorted_array [i], sorted_array [left], sorted_array [right]])
                    while left < right and sorted_array [left] == sorted_array [left + 1]:
                        left += 1
                    while left < right and sorted_array [right] == sorted_array [right -1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum_left_right < target:
                    left += 1
                else:
                    right -= 1
        return result

                






        
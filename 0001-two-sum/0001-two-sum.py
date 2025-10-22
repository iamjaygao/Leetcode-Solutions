class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        result = []
        for i, num in enumerate(nums):
            difference = target - num
            if difference in count:
                result.append(i)
                result.append(count[difference])
                count[difference] -= 1
            else:
                count[num] = i
        return result
            

            
                

            
        
      

        
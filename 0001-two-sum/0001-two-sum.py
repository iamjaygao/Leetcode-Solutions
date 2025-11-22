class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        result = []
        for i, val in enumerate(nums):
            diff = target - val 
            if diff in dic:
                result.append(dic[diff])
                result.append(i)
            else:
                dic[val] = i
        return result 
            


            
                

            
        
      

        
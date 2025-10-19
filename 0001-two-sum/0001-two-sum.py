class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        set_ = {}
        res = []
        n = len(nums)
        for i in range(n):
            key = target - nums[i]
            if key in set_:
                res.append(i)
                res.append(set_[key])
                del set_[key]
            else:
                set_[nums[i]] = i
        return res


            
                

            
        
      

        
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        
        def dfs(start, curr_sum, combin):
            if curr_sum == n and len(combin) == k:
                return result.append(combin[:])

            if curr_sum > n or len(combin) >= k:
                return 

            for i in range(start, 10):
                combin.append(i)
                dfs(i+1, curr_sum + i, combin)
                combin.pop()
      
                

        dfs(1, 0, [])
        return result

        
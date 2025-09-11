class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # initialize result list to store valid combination
        result = []
        
        # backtracking function
        def dfs(start, curr_sum, combin):
            """
            start: first number to consider(avoid duplicates and ensure order)
            curr_sum=m:  current accumulated sum
            combin: current comnination of numbers
            """

            # termination conditions: valid combintaion found
            if curr_sum == n and len(combin) == k:
                return result.append(combin[:]) #[:]create copy of current combination

            #pruning: stop if sum exceeds or combination size exceeds k
            if curr_sum > n or len(combin) >= k:
                return 

            # Explore all possibilities from current start positon
            for i in range(start, 10):  # numbers from start to 9
                combin.append(i)        # choose current number

                # recursively explore with next numbers (num+1 prevents duplicates)
                dfs(i+1, curr_sum + i, combin)
                combin.pop()   #backtrack: remove last number
      

        # start backtracking from number 1 with initial sum 0 and empty combination    
        dfs(1, 0, [])
        return result

        
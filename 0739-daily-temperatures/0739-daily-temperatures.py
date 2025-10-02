class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        for t in range(n):
            while stack and temperatures[stack[-1]] < temperatures[t]:
                pre_t = stack.pop()
                answer[pre_t] = t - pre_t
            stack.append(t)
        return answer




        
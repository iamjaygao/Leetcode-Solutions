class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0:
                if abs(ast) > stack[-1]:
                    stack.pop()
                    continue
                elif abs(ast) == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(ast)
        return stack


        
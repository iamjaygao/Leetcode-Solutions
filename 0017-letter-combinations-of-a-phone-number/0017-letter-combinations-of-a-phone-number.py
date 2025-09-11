class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # edge case handle
        if not digits:
            return []

        # direct used to handle the map
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # used to save the result
        result = []

        # calculate the length of the digits
        n = len(digits)

        # deep first search used to find the leaves which is the final answer as an elements in the new array
        def dfs(idx, comb):

            # base case, if the size of numbers equals to the size of output string
            # like,if you input '23', the size is 2, and the size of output should be 2
            # like 'ae', 'bf'....
            if idx == n:
                result.append(''.join(comb))
                return
            
            # get the current digit, which is a string type
            # get the letter based on the given digit via digit_map
            current_digit = digits[idx]
            letters = digit_map[current_digit]

            # iterate letters based on current given digit
            for letter in letters:
                comb.append(letter)         #push the current letter to the comb
                dfs(idx + 1, comb)          #recursively call the dfs until reach the base case, and return the final element, and append to the result.
                comb.pop()                  # pop the last element of the for the next iteration
        dfs(0, [])
        return result


        
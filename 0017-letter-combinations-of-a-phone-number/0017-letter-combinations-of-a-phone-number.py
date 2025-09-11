class Solution:
    def __init__(self):
        self.letterMap =[
            "",          #0
            "",          #1
            "abc",      #2
            "def",       #3
            "ghi",       #4
            "jkl",       #5
            "mon" ,      #6
            "pqrs",      #7
            "tuv",       #8
            "wxyz",     #9
        ]
        self.result = []
        self.s =""

    # index here used to track the digit in digits
    def backtracking(self, digits, index):
        if index == len(digits):
            self.result.append(self.s)
            return 
        digit = int(digits[index])
        letters = self.letterMap[digit]
        for i in range(len(letters)):
            self.s += letters[i]
            self.backtracking(digits, index+1)
            self.s = self.s[:-1]


    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return self.result
        self.backtracking(digits, 0)
        return self.result


        
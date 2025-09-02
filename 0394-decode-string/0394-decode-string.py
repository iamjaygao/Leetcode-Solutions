class Solution:
    def decodeString(self, s: str) -> str:
        numStack = []
        strStack = []

        curr_num = 0
        curr_str = ''

        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                numStack.append(curr_num)
                strStack.append(curr_str)
                curr_num = 0
                curr_str = ''
            elif c == ']':
                temp = numStack.pop()
                pre_str = strStack.pop()
                curr_str = pre_str + temp * curr_str
            else:
                curr_str = curr_str + c
     
        return curr_str





        
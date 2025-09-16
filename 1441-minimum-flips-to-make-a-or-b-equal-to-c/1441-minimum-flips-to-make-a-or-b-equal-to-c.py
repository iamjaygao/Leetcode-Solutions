class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            c_bit = (c >> i) & 1

            curr_or = a_bit | b_bit

            if curr_or != c_bit:
                if c_bit == 1:
                    flips += 1 
                else:
                    if a_bit == 1:
                        flips += 1
                    if b_bit == 1:
                        flips += 1
        return flips


        
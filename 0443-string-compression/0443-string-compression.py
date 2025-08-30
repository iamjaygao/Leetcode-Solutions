class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0
        n = len(chars)

        while read < n:
            char = chars[read]
            count = 0
            while read < n and char == chars[read]:
                count += 1
                read += 1
            chars[write] = char
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        
        return write

                




            



                



class Solution:
    def reverse(self, x: int) -> int:
        str_num = str(abs(x))
        str_num = int(str_num[::-1])

        if x < 0:
            str_num =  str_num*-1
            
        if str_num < -2**31 or str_num > 2**31:
            return 0
        else:
            return str_num

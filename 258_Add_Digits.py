class Solution:
    def addDigits(self, num: int) -> int:
        res = 0
        s = str(num)
        while len(s) != 1:
            for i in s:
                res += int(i)
            s = str(res)
            res = 0
        return int(s)

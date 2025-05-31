class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        res = False
        for i in range(32):
            if 4**i == n:
                res = True
        return res
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        res = False
        for i in range(32):
            if 3**i == n:
                res = True
        return res
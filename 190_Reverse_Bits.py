class Solution:
    def reverseBits(self, n: int) -> int:
        b = bin(n)
        b = format(n, '032b')
        rev = b[::-1]
        res = int(rev, 2)
        return res

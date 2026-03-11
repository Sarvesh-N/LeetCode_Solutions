class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_val = bin(n)[2:]
        res = ''
        for i in bin_val:
            if i == '0':
                res += '1'
            else:
                res += '0'
        return int(res, 2)

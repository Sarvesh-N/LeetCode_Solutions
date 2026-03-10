class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumofn = 0
        productofn = 1

        for i in str(n):
            sumofn += int(i)
            productofn *= int(i)

        total = sumofn + productofn

        if n % total == 0:
            return True
        return False

class Solution:
    def isBalanced(self, num: str) -> bool:
        arr = [int(i) for i in num]
        even = 0
        odd = 0
        n = len(arr)

        for i in range(n):
            if i % 2 == 0:
                even += arr[i]
            else:
                odd += arr[i]
        return even == odd

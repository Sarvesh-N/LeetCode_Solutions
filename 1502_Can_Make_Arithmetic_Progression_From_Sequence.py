class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        res = False
        arr.sort(reverse = True)
        seen = set()

        for i in range(1, len(arr)):
            seen.add(arr[i-1] - arr[i])
        return len(seen) == 1

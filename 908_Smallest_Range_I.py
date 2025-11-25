class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_v = min(nums)
        max_v = max(nums)
        diff = 0

        Max = max_v - k
        Min = min_v + k

        diff = Max - Min

        if diff <= 0:
            return 0
        return diff

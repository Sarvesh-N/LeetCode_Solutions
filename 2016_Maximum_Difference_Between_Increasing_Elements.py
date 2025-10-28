class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff = []
        min_v = nums[0]
        max_v = 0
        diff_val = 0
        for i in range(1, len(nums)):
            min_v = min(min_v, nums[i-1])
            if nums[i] > min_v:
                diff_val = nums[i] - min_v
                max_v = max(max_v, diff_val)
        return max_v if max_v > 0 else -1

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = 0
        for i in range(len(nums)):
            if target <= nums[i]:
                res = i
                break
            elif target not in nums:
                res = len(nums)
        return res

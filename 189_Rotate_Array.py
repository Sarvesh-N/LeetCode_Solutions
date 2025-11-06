class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
            """
            Do not return anything, modify nums in-place instead.
            """
            if len(nums) > k:
                last = nums[-k:]
                first = nums[:-k]
                nums[:] = last+first
            else:
                k = k%len(nums)
                last = nums[-k:]
                first = nums[:-k]
                nums[:] = last+first

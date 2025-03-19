class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = False
        nums.sort()

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                res = True
        return res
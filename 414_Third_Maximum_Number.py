class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse = True)
        res = 0
        if len(nums)>=3:
            res = nums[2]
        else:
            res = nums[0]
        
        return res

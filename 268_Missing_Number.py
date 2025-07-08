class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new_nums = [i for i in range(0,len(nums)+1)]
        res = list(set(new_nums)-set(nums))
        return res[0]

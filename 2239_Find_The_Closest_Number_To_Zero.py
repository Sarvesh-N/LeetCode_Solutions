class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]

        for i in nums:
            if abs(i) < abs(res):
                res = i
            elif abs(i) == abs(res) and i > res:
                res = i          
        return res
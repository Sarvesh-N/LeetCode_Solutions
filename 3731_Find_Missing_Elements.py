class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        new = []
        res = []
        for i in range(min(nums), max(nums) + 1 , 1):
            new.append(i)
        for i in new:
            if i not in nums:
                res.append(i)
        return res

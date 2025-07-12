class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        val = 0
        for i in nums:
            val+=i
            res.append(val)
        return res

        

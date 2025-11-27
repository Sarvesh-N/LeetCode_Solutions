class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        new  = {}
        res = True
        for i in nums:
            if i in new:
                new[i] += 1
            else:
                new[i] = 1
        
        for key, value in new.items():
            if value > 2:
                res = False
                break
        return res

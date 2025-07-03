class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res = 0
        """nums_copy = nums.copy()
        nums_copy.sort()
        peak = nums_copy[-1]

        for i in range(0,len(nums)-1):
            if nums[i] == peak:
                res = i
                break
        return res"""

        for i in range(0, len(nums)-1):
            if i == 0 and nums[0]>nums[1]:
                res = i
                break
            elif i == len(nums)-2 and nums[-1]>nums[-2]:
                res = len(nums)-1
                break
            elif nums[i] > nums[i+1] and nums[i]>nums[i-1]:
                res = i
                break
        return res     
        
            
            
        

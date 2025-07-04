class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # brute force
        """nums_squared = []
        for i in nums:
            nums_squared.append(i**2)
        return sorted(nums_squared)"""

        # two pointers
         left = 0
        right = len(nums)-1
        result = []
        while left<=right:
            if abs(nums[left]) > abs(nums[right]):
                result.append(nums[left]**2)
                left+=1
            else:
                result.append(nums[right]**2)
                right-=1
        result.reverse()
        return result
        

        

        

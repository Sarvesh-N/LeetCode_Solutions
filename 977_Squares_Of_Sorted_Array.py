class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_squared = []
        for i in nums:
            nums_squared.append(i**2)
        return sorted(nums_squared)

        

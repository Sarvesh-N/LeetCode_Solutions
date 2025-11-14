class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        seen = set()
        for i in nums:
            if i != 1:
                count = 0
            elif i == 1:
                count += 1
            seen.add(count)
        return max(seen)

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = {}
        new = []
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for i, j in seen.items():
            if j == 2:
                new.append(i)
        return new

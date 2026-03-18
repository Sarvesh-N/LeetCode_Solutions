class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        freq = {}
        for i in nums :
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for i in nums:
            if i % 2 == 0:
                if freq[i] ==  1:
                    return i
        return -1

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        max_values = 0
        for i in seen.values():
            max_values = max(max_values, i)
        key_max = [k for k, v in seen.items() if v == max_values]

        str_val = []
        for i in key_max:
            str_val.append(str(i))
        return len(max_values * key_max)

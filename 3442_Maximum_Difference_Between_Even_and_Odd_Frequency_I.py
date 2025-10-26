class Solution:
    def maxDifference(self, s: str) -> int:
        seen = {}
        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        even = []
        odd = []
        for i in seen.values():
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        min_even = min(even)
        max_odd = max(odd)
        return max_odd - min_even
        

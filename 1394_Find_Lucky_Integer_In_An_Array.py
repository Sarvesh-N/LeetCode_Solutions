from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        count = Counter(arr)
        for i, j in count.items():
            if i == j:
                res = max(res, i)
        return res

                

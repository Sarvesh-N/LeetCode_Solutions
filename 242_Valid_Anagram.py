from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = False
        if len(s)!=len(t):
            return False
        elif Counter(s) == Counter(t):
            res = True
        return res

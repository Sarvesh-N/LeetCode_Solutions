class Solution:
    def makeFancyString(self, s: str) -> str:
        res = set()
        new = ""
        for i in range(len(s)-2):
            if s[i] == s[i+1]:
                if s[i+1] == s[i+2]:
                    res.add(i+2)
        for j in range(len(s)):
            if j not in res:
                new += s[j]
        return new

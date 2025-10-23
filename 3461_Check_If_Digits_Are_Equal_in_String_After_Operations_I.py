class Solution:
    def hasSameDigits(self, s: str) -> bool:
        vals = [int(i) for i in s]
        n = len(vals)
        while n>2:
            new = []
            for i in range(len(vals)-1):
                new.append((vals[i]+vals[i+1])%10)
            n = len(new)
            vals = new
        if vals[0] == vals[1]:
            return True
        else:
            return False 

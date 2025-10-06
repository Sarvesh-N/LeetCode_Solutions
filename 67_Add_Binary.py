class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = int(a, 2)
        m = int(b, 2)
        fin = n+m
        
        return bin(fin)[2:]
                
        

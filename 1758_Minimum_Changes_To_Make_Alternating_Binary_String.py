class Solution:
    def minOperations(self, s: str) -> int:
        starts0 = 0
        starts1 = 0

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '0':
                    starts1 +=1
                else:
                    starts0 += 1
            else:
                if s[i] == '1':
                    starts1 += 1
                else :
                    starts0 += 1
        return min(starts0, starts1)

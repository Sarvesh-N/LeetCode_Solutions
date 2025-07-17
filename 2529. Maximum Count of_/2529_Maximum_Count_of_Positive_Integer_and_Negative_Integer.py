class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = []
        neg = []
        for i in nums:
            if i > 0:
                pos.append(i)
            elif i < 0:
                neg.append(i)
        return len(pos) if len(pos) > len(neg)  else len(neg)        


        
        

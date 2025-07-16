class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nums1 = []
        nums2 = []
        val1 = 0
        val2 = 0
        for i in range(n+1):
            if i%m !=0:
                #nums1.append(i)
                val1+=i
            else:
                #nums2.append(i)
                val2+=i
        return val1-val2            
        

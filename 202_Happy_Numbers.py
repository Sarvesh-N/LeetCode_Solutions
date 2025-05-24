class Solution:
    def isHappy(self, n: int) -> bool:
        list1 = []
        seen = set()
        while n!= 1:
            list1.clear()
            for i in str(n):
                list1.append(i)
            n = 0
            for i in list1:
                n+=pow(int(i),2)
            if n in seen:
                break
            seen.add(n)
        if n ==1:
            return True
        else:
            return False


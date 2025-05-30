class Solution:
    def isValid(self, s: str) -> bool:
        list1 = []
        res = True
        openings = ['(','[','{']
        closings = [')',']','}']
        matches = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for i in s:
            if i in openings:
                list1.append(i)
            if i in closings:
                if list1 and list1[-1] == matches[i]:
                    list1.pop()
                else :
                    res = False
        return res and len(list1) == 0
                 
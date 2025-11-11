class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        set_arr = set()
        res = False

        for i in arr:
            if i*2 in set_arr or i/2 in set_arr:
                res = True
                break
            else:
                set_arr.add(i)
        return res

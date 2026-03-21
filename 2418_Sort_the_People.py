class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        new = dict(zip(heights, names)) 
        heights.sort(reverse = True)
        res = []
        for i in heights:
            for key, value in new.items():
                if key == i:
                    res.append(value)
        return res

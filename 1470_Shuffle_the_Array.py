class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[:n]
        y = nums[n:]
        res = []
        # for i in nums[:n]:
        #     x.append(i)
        # for i in nums[n:]:
        #     y.append(i)
        for a, b in zip(x, y):
            res += [a, b]
        return res

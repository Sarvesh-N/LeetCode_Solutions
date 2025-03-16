class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_of_nums = set(nums)
        nums.clear()

        for i in set_of_nums:
            nums.append(i)
        nums.sort()
        print(nums)
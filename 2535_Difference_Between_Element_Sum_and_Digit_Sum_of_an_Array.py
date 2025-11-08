class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        # str_nums = [str(i) for i in nums]
        # digit_list = []
        # for i in str_nums:
        #     if len(i) != 1:
        #         first = int(i)//10
        #         last = int(i)%10
        #         digit_list.append(first)
        #         digit_list.append(last)
        #     else:
        #         digit_list.append(int(i))
        # return sum(nums) - sum(digit_list)
        str_nums = [str(i) for i in nums]
        digits = []
        for i in str_nums:
            if len(i) != 1:
                for j in i:
                    digits.append(int(j))
            else:
                digits.append(int(i))
        return sum(nums) - sum(digits)


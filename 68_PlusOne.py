"""
# this is the 1st approach

nums = [1,2,3,4]

for i in nums:
    if nums[-1] == 9:
        nums.remove(i)
        nums.append(i)
    else:
        nums.remove(i)
        nums.append(i)
print(nums)"""

# 1st approach
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_s = ""
        list1 = []
        for i in digits:
            str_s += str(i)
        str_s = int(str_s)+1
        for i in str(str_s):
            list1.append(int(i))
        return list1  

# 2nd approach
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_list = [str(i) for i in digits]
        joined = "".join(str_list)
        joined_final = str(int(joined)+1)
        arr = [int(i) for i in joined_final]
        return arr



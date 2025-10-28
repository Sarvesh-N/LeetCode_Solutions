class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hillvalley = 0
        new = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                pass
            else:
                new.append(nums[i])
        for i in range(1, len(new)-1):
            if (new[i] > new[i-1] and new[i] > new[i+1]) or (new[i] < new[i-1] and new[i] < new[i+1]):
                hillvalley+=1
        
        return hillvalley

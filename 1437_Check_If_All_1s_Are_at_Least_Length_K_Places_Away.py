class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        seen = []
        first_pos = -1
        last_pos = -1
        count = 0
        have_one = False      

        for i in range(len(nums)):
            if nums[i] == 1:
                if first_pos == -1:
                    first_pos = i
                last_pos = i

        if first_pos == -1 or first_pos == last_pos:
            return True
    
        for i in nums[first_pos:last_pos+1]:
            if i == 1:
                if count == 0 and have_one:   
                    seen.append(0)
                if count > 0:
                    seen.append(count)
                count = 0
                have_one = True                
            else:
                count += 1
    
        for i in seen:
            if i < k:
                return False
        return True
